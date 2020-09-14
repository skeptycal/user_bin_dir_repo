#!/usr/bin/env python3

import sys

from dataclasses import dataclass, field, Field
from os import linesep as NL, PathLike
from pathlib import Path
import typing as t

from loguru import logger

FileType = t.TypeVar('A', str, bytes, int)

# set -a


# @dataclass
# class TextFile(list):

SAMPLE_NAME: PathLike = '/Users/michaeltreanor/Documents/coding/user_bin_dir_repo/src/python/dupe_sample.txt'


def get_file(filename: FileType):
    with Path(filename).open(mode='rb') as fh:
        return fh.read().


s = get_file(SAMPLE_NAME)


for i in s:
    print(str(i))
