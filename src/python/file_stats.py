#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# file_stats.py

# examples from: https://www.programcreek.com/python/example/5779/io.TextIOWrapper

import sys

from dataclasses import dataclass, field, Field
from pathlib import Path
from typing import List, Sequence

from auto_loguru import logger


class Words:
    FILE_MODES = {
        "r": sys.stdin,
        "rb": sys.stdin.buffer,
        "w": sys.stdout,
        "wb": sys.stdout.buffer,
    }

    def _fopen(self, fname, mode):
        """
        Extend file open function, to support
            1) "-", which means stdin/stdout
            2) "$cmd |" which means pipe.stdout
        """
        if not fname:
            return None
        fname = fname.rstrip()
        if fname == "-":
            try:
                return self.FILE_MODES[mode]
            except KeyError:
                raise ValueError(f"Unknown open mode: {mode}")

        elif fname[-1] == "|":
            pin = self._fopen(fname[:-1], mode, background=(mode == "rb"))
            return pin if mode == "rb" else TextIOWrapper(pin)
        else:
            if mode in ["r", "rb"] and not os.path.exists(fname):
                raise FileNotFoundError("Could not find common file: {}".format(fname))
            return open(fname, mode)

    def popen(cmd, mode="r", buffering=-1):
        # Helper for popen() -- a proxy for a file whose close waits for the process
        if not isinstance(cmd, str):
            raise TypeError("invalid cmd type (%s, expected string)" % type(cmd))
        if mode not in ("r", "w"):
            raise ValueError("invalid mode %r" % mode)
        if buffering == 0 or buffering is None:
            raise ValueError("popen() does not support unbuffered streams")
        import subprocess, io

        if mode == "r":
            proc = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, bufsize=buffering
            )
            return _wrap_close(io.TextIOWrapper(proc.stdout), proc)
        else:
            proc = subprocess.Popen(
                cmd, shell=True, stdin=subprocess.PIPE, bufsize=buffering
            )
            return _wrap_close(io.TextIOWrapper(proc.stdin), proc)

    def __iter__(self):
        import csv
        import subprocess
        from io import TextIOWrapper

        import sys

        if self.program.endswith(".py"):
            # If it is a python program, it's really nice, possibly required,
            # that the program be run with the same interpreter as is running this program.
            #
            # The -u option makes output unbuffered.  http://stackoverflow.com/a/17701672
            prog = [sys.executable, "-u", self.program]
        else:
            prog = [self.program]

        p = subprocess.Popen(
            prog + self.options, stdout=subprocess.PIPE, bufsize=1, env=self.env,
        )

        yield from csv.reader(
            TextIOWrapper(p.stdout, encoding="utf8", errors="replace")
        )

    def next_filehandle(self):
        """Go to the next file and retrun its filehandle or None (meaning no more files)."""
        filename = self.next_filename()
        if filename is None:
            fhandle = None
        elif filename == "-":
            fhandle = io.TextIOWrapper(sys.stdin.buffer, encoding=self.encoding)
        elif filename == "<filehandle_input>":
            fhandle = self.filehandle
        else:
            filename_extension = filename.split(".")[-1]
            if filename_extension == "gz":
                myopen = gzip.open
            elif filename_extension == "xz":
                myopen = lzma.open
            elif filename_extension == "bz2":
                myopen = bz2.open
            else:
                myopen = open
            fhandle = myopen(filename, "rt", encoding=self.encoding)
        self.filehandle = fhandle
        return fhandle

    def toprettyxml(self, indent="\t", newl="\n", encoding=None):
        if encoding is None:
            writer = io.StringIO()
        else:
            writer = io.TextIOWrapper(
                io.BytesIO(),
                encoding=encoding,
                errors="xmlcharrefreplace",
                newline="\n",
            )
        if self.nodeType == Node.DOCUMENT_NODE:
            # Can pass encoding only to document, to put it into XML header
            self.writexml(writer, "", indent, newl, encoding)
        else:
            self.writexml(writer, "", indent, newl)
        if encoding is None:
            return writer.getvalue()
        else:
            return writer.detach().getvalue()


# with open("/usr/share/dict/words") as fp:
#     w = len(fp.read)
#     print(len(w))
#     print(w.readline())


def word_count(file_name: str) -> int:
    retval: int = 0
    try:
        retval = sum(1 for word in open(file_name).read())

    except:
        pass
    return retval


def line_count(file_name: str) -> int:
    retval: int = 0
    try:
        retval = len(open(file_name).readlines())
    except:
        pass
    return retval
    # return sum(1 for line in open(file_name).readlines()))


args: List[str] = []

# use stdin if it's full
if not sys.stdin.isatty():
    input_stream = sys.stdin
    args = sys.stdin.readlines()

if not args:
    args = sys.argv[1:]

if not args:
    args = ["/usr/share/dict/words"]
    # logger.info(args)

print(f"file name                     lines           words")
print("-" * 60)


class FileStatsError(IOError):
    """ An error occurred while collecting file stats. """


@dataclass
class Stats:
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    def words(self):
        if not self._words:
            try:
                self._words = sum(1 for _ in self.path.open.read())
            except:
                self._words = 0
        return self._words

    @property
    def data(self):
        if not self._data:
            self._data = self._path.open(mode="r").readlines()
        return self._data

    @property
    def name(self) -> str:
        if not self._name:
            self._name = self._path.name
        return self._name

    @property
    def path(self) -> Path:
        if not self._path:
            self._path = Path(self.file_name).resolve()
        return self._path

    @property
    def parent(self) -> str:
        if not self._parent:
            self._parent = self.path.parent
        return self._parent

    @property
    def parents(self) -> List[str]:
        if not self._parents:
            self._parents = self.path.parents


@dataclass
class FileList(list):
    name: str = "filelist"
    args: Field = field(init=False)

    def __post_init__(self):
        self.args = self._get_args()
        if self.args:
            for arg in self._get_args():
                if Path(arg).is_file():
                    self.append(Stats(arg))
        else:
            raise FileStatsError()

    def _get_args(self):
        args: List[str] = []

        # use stdin if it's full
        if not sys.stdin.isatty():
            input_stream = sys.stdin
            self.extend(sys.stdin.readlines())

        elif not self:
            if argv[1:]:
                self.extend(argv[1:])
            else:
                self = ["/usr/share/dict/words"]


for arg in args:
    arg = arg.strip()
    st = Stats(arg)
    logger.info(st.words())
    if not (name := Path(arg)).is_file():
        continue
    name = f"..{name.parent}{name.name}"
    lc = line_count(arg)
    wc = word_count(arg)
    # data.append = Stats(arg)
    print(f"{name:<25.25} ... {line_count(arg):>15} {word_count(arg):>15}")
