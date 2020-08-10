#!/usr/bin/env python3

from string import whitespace
from pathlib import Path
from sys import path as PYTHON_PATH


PYTHON_PATH.insert(-1,Path(__file__).resolve().parents[0].as_posix())
PYTHON_PATH.insert(-1,Path(__file__).resolve().parents[1].as_posix())

PYTHON_PATH = list(set(PYTHON_PATH))


# import html2txt
# from html2txt import onlywhite2, onlywhite

class TestOnlyWhite:
    def test_only_white_vs_isspace(self):
        lines=[
            ' df sdwlkjlkd9788723',
            '    ',
            '\n',
            ' sdfkkj     ',
            '\t\t   '
            ]

        for c in lines:
            # for c in line:
            print(f"{c.isspace():<10} - {onlywhite(c):10} - {onlywhite2(c):<10}")
            # print(c.isspace())
            # print(onlywhite(c))
            # print(onlywhite2(c))
            # assert c.isspace() == onlywhite(c)
                # assert (onlywhite(c) == c in whitespace)
                # assert (onlywhite(c) == c.isspace())

print(repr(whitespace))
