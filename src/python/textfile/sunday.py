#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# shellcheck source=/dev/null
# shellcheck disable=2230,2086

# import autosys
import datetime
from appdirs import AppDirs, appauthor, appname, prop
from dataclasses import dataclass


APPNAME = 'IsSunday'
APPAUTHOR = 'Skeptycal'
VERSION = '1.0.0'


if __name__ == '__main__':  # if script is loaded directly from CLI

    ap = AppDirs(appname=APPNAME, appauthor=APPAUTHOR,
                 version=VERSION, roaming=True, multipath=True)

    d = NowAndThen()

    d.check()

    print(d)
    print(d.weekday)
    print(d.daynum)
    print(d.timestamp)
