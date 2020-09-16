#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if True:  # ? -----------------------------> Imports
    import codecs
    import os
    import sys
    import mmap

    from pathlib import Path
    from datetime import datetime as dt
    from dataclasses import dataclass
    from io import TextIOWrapper
    from os import PathLike
    from pprint import pprint
    from functools import lru_cache

    from collections import Counter

    from loguru import logger

    from ._anyfile import AnyFile
    from ._exceptions import AnyFileError, BytesFileError, TextFileError, TextFileEncodingError

    from typing import AnyStr, List


if True:  # ? -----------------------------> Constants and Imported Functions
    now: dt = dt.now()
    year: int = now.year
    AUTHOR: str = 'Michael Treanor'

    DEFAULT_COMMENT_STRING: str = '#'
    SECTION_FLAG: str = '#? ----------------------------->'
    DEFAULT_TEMPLATE_FLAG: str = "#? ----------------------------->' copyright (c)"
    TEMPLATE_END_FMT: str = "#? ###################### copyright (c) {} {} #################"

    DEFAULT_HEADER_FILE_NAME: str = 'default_textfile_header.sh'
    PY3_SHEBANG: str = '''#!/usr/bin/env python3
    '''

    ZSH_SHEBANG: str = '''#!/usr/bin/env zsh
    # -*- coding: utf-8 -*-
        # shellcheck shell=bash
        # shellcheck source=/dev/null
        # shellcheck disable=2178,2128,2206,2034
    '''


class BasicColors:
    ATTN = "\u001b[38;5;178m"
    BLACK = "\u001b[30m"
    LIGHTBLUE = "\u001b[34m"
    BLUE = "\u001b[38;5;38m"
    CANARY = "\u001b[38;5;226m"
    CHERRY = "\u001b[38;5;124m"
    COOL = "\u001b[38;5;38m"
    CYAN = "\u001b[36m"
    GO = "\u001b[38;5;28m"
    GREEN = "\u001b[32m"
    LIME = "\u001b[32;1m"
    MAGENTA = "\u001b[35m"
    MAIN = "\u001b[38;5;229m"
    PURPLE = "\u001b[38;5;93m"
    RAIN = "\u001b[38;5;93m"
    RED = "\u001b[31m"
    RESET = "\u001b[0m"
    WARN = "\u001b[38;5;203m"
    WHITE = "\u001b[37m"
    YELLOW = "\u001b[33m"


bc = BasicColors()


def main():
    template_end: str = TEMPLATE_END_FMT.format(year, AUTHOR)

    SAMPLE_FILE: str = 'test_zsh_boot.log'
    HEADER_FILE: str = "dotfiles_header.sh"

    def ls(path_name: PathLike = '.'):
        for _, _, files in os.walk(path_name):
            for f in files:
                print(f)

    # ls()

    print()
    fh = TextFile(filename=SAMPLE_FILE)
    print(f"{fh.filename=}")
    print()
    # print(fh.head(2))
    # print()
    # print(fh.tail(2))
    # print()
    print(f"{fh._count('SUCCESS')=}")
    print(f"{fh._count('source')=}")
    print(f"{fh._count('zsh')=}")
    print(f"{fh._count('highlighter')=}")
    # print(fh._count('\n'))
    print(fh.counter('SUCCESS'))
    print(f"{fh.length=}")
    # print(fh.data)
    print(f"{fh.word_count()=}")

    print()
    # print(fh.make_comment('fdajd'))
    # pprint(fh.remove_comments())
    # print(fh.lines())
    pprint(fh)


class BytesFile(AnyFile):

    @property
    def data(self) -> bytes:
        """ lazy load bytes from bytes file as needed """
        if not self._data:
            try:
                with self.path.open(mode='rb') as fd:
                    self._data = fd.read()
            except:
                raise BytesFileError(
                    f'The path {self.filename} could not be loaded. ')

        return self._data


class MmapFile(AnyFile):

    def mem_map(self):
        with self.path.open(mode="r+b") as fd:
            self._data = mmap.mmap(fileno=fd.fileno, length=0)

    # TODO - override methods for use with mmap files...


@dataclass
class TextFile(AnyFile):
    """ Text File with automatic addition and modifications.

        Allow search/replace of regex keys, entire lines, or sections
        Allow additions and deletions (before or after flags)
        Change keys or values

        """
    template_end_flag: str = DEFAULT_TEMPLATE_FLAG
    comment_string: str = DEFAULT_COMMENT_STRING
    header_filename: str = DEFAULT_HEADER_FILE_NAME
    _length: int = 0
    _header: List[AnyStr] = list


# * file operations for text file


    def line_clean(self, line: str, repl: str = ' ') -> str:
        for char in line:
            if not char.isprintable():
                line.replace(char, repl)
        return line

    def lines(self, check_errors: bool = True, ignore_errors: bool = True, repl: str = ' ') -> List[str]:
        """ Lazy load lines from text file as needed.

            - check_errors    - check for non-printable characters
            - ignore_errors   - replace non-printable characters
            - repl            - string used to replace non-printable characters
            """
        if not self:
            with open(self.path) as _:
                self = _.readlines()
        if check_errors:
            for i, line in enumerate(self):
                if not line.isprintable():
                    if not ignore_errors:
                        raise TextFileEncodingError(
                            f'An encoding error occurred while reading a line from {self.short_name}.')
                    line = self.line_clean(line, repl=repl)
                self.pop(i)
                self.insert(i, line)
        return self

        return [str(_) for _ in super().lines]
        if not self:
            self.clear()
            with open(self.path) as _:
                self.extend(_.readlines())
        return self

    @property
    def refresh(self) -> List[AnyStr]:
        """ clear line list and reload from file """
        self.clear()
        return self.lines

    def _load_header(self) -> AnyStr:
        """ lazy load the default header from a file. """
        with open(self._header_filename) as _:
            self._header = _.read()
        return self._header

    def writelines(self) -> int:
        try:
            with open(self.path, mode='wt') as _:
                _.writelines(self.lines)
            return 0
        except OSError as e:
            logger.error(e)
            return 1
            # raise

    @property
    def data(self) -> str:
        """ lazy load text from text file as needed """
        return str(super().data)

    def no_white(self) -> str:
        """ Return file data with all duplicate whitespace normalized. """
        return ' '.join(str(self.data).split())

    def lines_no_white(self) -> List[str]:
        return [_.strip() for _ in self.lines]

        # * sorting and utility operations for text files

    @property
    def length(self) -> int:
        if not self._length:
            self._length = len(self.lines)
        return self._length

    def head(self, n: int = 5):
        return self[:n]

    def tail(self, n: int = 5):
        return self[-n:]

    def _count(self, needle: AnyStr) -> int:
        """ Count occurrences of individual 'needle' strings in all lines """
        return sum(bool(x) for x in self if needle in x)

    def line_count(self, line_needle: AnyStr) -> int:
        """ Count occurrences of 'line_needle' as complete, exact lines """
        return self.count(line_needle)

    @lru_cache
    @property
    def counter(self, needle: AnyStr) -> int:
        """ Using a Counter to count entire identical lines
            """
        return Counter(self)

    def line_counter(self, needle_line: AnyStr) -> int:
        """ Use Counter to count occurrences of 'line_needle' as complete,
            exact lines. """
        return self.counter[needle_line]

    def word_count(self) -> int:
        return

# * edit header in text file

    @ property
    def header_index(self) -> int:
        ''' return index of header end flag or 0 if none is found '''
        for i, line in enumerate(self):
            if line == self.comment_str(self.end_flag):
                return i
        return 0

    @ property
    def header(self) -> List[AnyStr]:
        if not self._header:
            self._header = []

    def prune_header(self) -> List[AnyStr]:
        return self.lines[self.header_index()+1:]

    def get_header(self) -> List[AnyStr]:
        return self.lines[:self.header_index()]

    def place_header(self) -> List[AnyStr]:
        self.insert(0, self.header)
        return self

    # * edit lists of lines in text file

    def remove_comments(self) -> List[AnyStr]:
        return [x for x in self.lines if not x.startswith(self.comment_str)]

    def prune(self, _prune: AnyStr) -> List[AnyStr]:
        ''' remove 'prune' items '''
        return [x for x in self.lines if _prune in x]

    def purge(self, _keep: AnyStr) -> List[AnyStr]:
        ''' purge elements not containing 'keep' items '''
        return [x for x in self.lines if _keep in x]

    def blacklist(self, _blacklist: List) -> List[AnyStr]:
        ''' remove blacklisted items '''
        return [x for x in self.lines if x not in _blacklist]

    def whitelist(self, _whitelist: List) -> List[AnyStr]:
        ''' keep only whitelisted items '''
        return [x for x in self.lines if x in _whitelist]

    def starts(self, keep: bool = True) -> List[AnyStr]:
        pass

    # * edit individual lines in text file

    def make_comment(self, s: str):
        """ Add comment string to line. """
        return f"{self.comment_str}{s}"

    def undo_comment(self, s: str):
        """ Remove comment string at start of line. If comment string is
            not found at the start of the line (after removing whitespace),
            the original string is returned.
            """
        if s.rstrip().startswith(self.comment_str):
            return s.rstrip()[len(self.comment_str):]
        return s

        # class ZshHeader(Header):
        #     shebang: str = zsh_shebang
        #     comment_str: str = "#"


if __name__ == "__main__":
    main()

# SET_DEBUG=${SET_DEBUG:-0} # set to 1 for verbose testing
# set - a

# _debug_tests() {
# 	if (( SET_DEBUG == 1 )); then
# 		printf '%b\n' "${WARN:-}Debug Mode Details for ${CANARY}${0##*/}${RESET:-}"
# 		color_sample
# 	fi
# }
#? ###################### copyright (c) 2019 Michael Treanor #################
