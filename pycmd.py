#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" pycmd - run a shell command
  - with CLI args
  - catch exceptions
  - log the results (default is append to `sp.log`)
"""

from subprocess import check_output
from sys import argv

if len(argv) > 1:
    with open("sp.log", mode="at",) as f:
        f.write(argv[1:])
        f.write("=" * 79)
        try:
            f.write(check_output(argv[1:]).decode())
        except Exception as e:
            try:
                f.write(e)
            except:
                print(e)
        finally:
            f.write("-" * 79)
