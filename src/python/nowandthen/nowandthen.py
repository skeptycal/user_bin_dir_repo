from datetime import datetime as dt


class NowAndThen:
    """ Wrapper for the 'datetime' standard library module. """

    def __init__(self) -> None:
        dt.__init__(self)

    # ? ****************************** dates and times
    @ property
    def now(self) -> dt:
        return dt.now()

    @ property
    def date(self) -> dt.date:
        return self.now.date()

    @ property
    def time(self) -> dt.time:
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
        return self.weekday == 1

    # ? ****************************** tasks checks

    def check(self):
        if self.is_sunday:
            self.do_sunday_tasks()
        elif self.is_monday:
            self.do_monday_tasks()

    def do_sunday_tasks(self):
        print('Sunday')

    def do_monday_tasks(self):
        print('Monday')
