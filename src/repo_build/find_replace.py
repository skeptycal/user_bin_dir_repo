#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
import typing as t
from os import PathLike, linesep as NL, environ as ENV, stat_result
from sys import argv, stdout, stderr
from io import TextIOWrapper
from loguru import logger


def die(msg: str) -> None:
    """ Generic quick die with message. """
    logger.error(msg)
    print(msg)
    exit(msg)


def listdir(dirname):
    return sorted([os.path.join(dirname, i)
                   for i in os.listdir(dirname)])


def print_as_hex(s):
    """
    Print a string as hex bytes.

    Reference: https://github.com/audreyfeldroy/binaryornot/blob/master/binaryornot/helpers.py
    """
    print(":".join("{0:x}".format(ord(c)) for c in s))


_NUM_SIGNATURE_BYTES = 262


def get_signature_bytes(path):
    """
    Reads file from disk and returns the first 262 bytes
    of data representing the magic number header signature.
    Args:
        path: path string to file.
    Returns:
        First 262 bytes of the file content as bytearray type.

    Reference: https://github.com/h2non/filetype.py/blob/master/filetype/utils.py
    """
    with open(path, 'rb') as fp:
        return bytearray(fp.read(_NUM_SIGNATURE_BYTES))


def signature(array):
    """
    Returns the first 262 bytes of the given bytearray
    as part of the file header signature.
    Args:
        array: bytearray to extract the header signature.
    Returns:
        First 262 bytes of the file content as bytearray type.

    Reference: https://github.com/h2non/filetype.py/blob/master/filetype/utils.py
    """
    length = len(array)
    index = _NUM_SIGNATURE_BYTES if length > _NUM_SIGNATURE_BYTES else length

    return array[:index]


def get_bytes(obj):
    """
    Infers the input type and reads the first 262 bytes,
    returning a sliced bytearray.
    Args:
        obj: path to readable, file, bytes or bytearray.
    Returns:
        First 262 bytes of the file content as bytearray type.
    Raises:
        TypeError: if obj is not a supported type.

    Reference: https://github.com/h2non/filetype.py/blob/master/filetype/utils.py
    """
    try:
        obj = obj.read(_NUM_SIGNATURE_BYTES)
    except AttributeError:
        # duck-typing as readable failed - we'll try the other options
        pass

    kind = type(obj)

    if kind is bytearray:
        return signature(obj)

    if kind is str:
        return get_signature_bytes(obj)

    if kind is bytes:
        return signature(obj)

    if kind is memoryview:
        return signature(obj).tolist()

    raise TypeError('Unsupported type as file input: %s' % kind)


class ConfigFileError(Exception):
    """ An error occurred while processing configuration files. """


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logger.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)


@dataclass
class PathObject:
    """ The base wrapper for a Path object that performs minimum checks
        and provides minimum common methods.
        """
    source_file: PathLike
    _name: str = ''
    _stat: stat_result = None
    _filesize: int = 0
    uid: int = 0
    gid: int = 0
    _inode: int = 0
    a_time: float = 0.0
    c_time: float = 0.0
    m_time: float = 0.0

# ? ############################################ Setup properties
    def __post_init__(self, *args, **kwargs) -> None:
        """ Perform checks, filtering, sorting, etc ... """
        # add other __init__ items here ...
        pass


# ? ############################################ Path properties

    @property
    def path(self) -> Path:
        """ lazy init variable """
        if not self._path:
            self._path = Path(self.source_file).resolve()
        return self._path

    @property
    def name(self) -> str:
        """ lazy init variable """
        if not self._name:
            self._name = self.path.name
        return self._name

    @property
    def container(self) -> Path:
        return self.path.parent

        @property
        def is_dir(self) -> bool:
            return self.path.is_dir()

# ? ############################################ Stat properties
    @property
    def stat(self) -> stat_result:
        """ lazy load variable """
        if not self._stat:
            self._stat = self.path.stat()
        return self._stat

    @property
    def size(self) -> int:
        """ lazy init variable """
        if not self._filesize:
            self._filesize = self.stat.st_size
        return self._filesize

    @property
    def inode(self) -> int:
        """ lazy init variable """
        if not self._inode:
            self._inode = self.stat.st_ino
        return self._inode

    @property
    def uid(self) -> int:
        return self.stat.st_uid

    @property
    def gid(self) -> int:
        return self.stat.st_gid

    @property
    def a_time(self) -> float:
        """ last access time """
        return self.stat.st_atime

    @property
    def c_time(self) -> float:
        """ creation time """
        return self.stat.st_ctime

    @property
    def m_time(self) -> float:
        """ last modification time """
        return self.stat.st_mtime


class ExistingPathObject(PathObject):
    """ A wrapper for an existing PathObject. Checks
        that the 'source_file' Path object exists.
        """

    def __post_init__(self, *args, **kwargs) -> None:
        """ Check that the source_file path exists ... """
        super().__post_init__(*args, **kwargs)

        self._path = Path(source_file).resolve()

        super().__init__(length, length)

        if not self._path.exists():
            raise ConfigFileError(
                f"The source file {self.path} does not exist...")


class TextFile(ExistingPathObject):

    def __post_init__(self):
        """ Check that the source_file path exists and is a text file ... """
        super().__post_init__()

    def is_text(self):
        import codecs

        codecs.

        #: BOMs to indicate that a file is a text file even if it contains zero bytes.
        _TEXT_BOMS = (
            codecs.BOM_UTF16_BE,
            codecs.BOM_UTF16_LE,
            codecs.BOM_UTF32_BE,
            codecs.BOM_UTF32_LE,
            codecs.BOM_UTF8,
        )

        def is_binary_file(source_path):
            with open(source_path, 'rb') as source_file:
                initial_bytes = source_file.read(8192)
            return not any(initial_bytes.startswith(bom) for bom in _TEXT_BOMS) \
                and b'\0' in initial_bytes

    def is_text_file(self) -> bool:
        try:
            with open(self.path, 'tr') as check_file:  # try open file in text mode
                check_file.seekable()
                return False
        except:  # if fail then file is non-text (binary)
            return True


class File(ExistingPathObject):

    def __init__(self):
        super().__init__(source_file=source_file)

        if not self.path.is_file():
            raise ConfigFileError(
                f"The source file {self.path} is not a regular file...")


class FileReplacements:
    pass


class ConfigFile(File):

    def replacements(self, reps: FileReplacements = None,):
        pass

    def do_replace(self):
        SOURCE_FILE = args[1]
        TARGET_FILE = f"{SOURCE_FILE}.bak"
        pass

    def __str__(self):
        """ This is an unusual __str__ method that returns the entire
            contents of the file instead of the more common file name.
            """
        return str(self.data)


class FileSet(list):
    file_set_name: str = ''

    def __init__(self):
        # maintain a list of files and config options

        # check for filename existance?
        #

    def __append__(self):
        if not Path(SOURCE_FILE).resolve().is_file:
            raise ConfigFileError(
                f"The source file {SOURCE_FILE} does not exist...")
