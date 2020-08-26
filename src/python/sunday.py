#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# shellcheck source=/dev/null
# shellcheck disable=2230,2086

# import autosys
import datetime
from datetime import datetime as dt
from appdirs import AppDirs, appauthor, appname, prop
from dataclasses import dataclass


APPNAME = "IsSunday"
APPAUTHOR = "Skeptycal"
VERSION = "1.0.0"


class NowAndThen:

    def __init__(self) -> None:
        pass

    # ? ****************************** dates and times
    @ property
    def now(self) -> dt:
        return dt.now()

    @ property
    def date(self) -> datetime.date:
        return self.now.date()

    @ property
    def time(self) -> datetime.time:
        return self.now.time()

    @ property
    def timestamp(self) -> float:
        return self.now.timestamp()

    # ? ****************************** datetime checks

    @ property
    def weekday(self) -> int:
        return self.now.isoweekday()

    @ property
    def daynum(self) -> int:
        return self.now.day

    @ property
    def is_weekday(self) -> bool:
        return self.weekday < 6

    @ property
    def is_sunday(self) -> bool:
        return self.weekday == 7

    @ property
    def is_monday(self) -> bool:
        return self.weekday == 2

    # ? ****************************** tasks checks

    def do_sunday_tasks(self):
        print("Sunday")

    def do_monday_tasks(self):
        print("Monday")


if __name__ == "__main__":  # if script is loaded directly from CLI

    ap = AppDirs(appname=APPNAME, appauthor=APPAUTHOR,
                 version=VERSION, roaming=True, multipath=True)

    d = NowAndThen()

    if d.is_sunday:
        d.do_sunday_tasks()
    elif d.is_monday:
        d.do_monday_tasks()

    print(d)
    print(d.weekday)
    print(d.daynum)
