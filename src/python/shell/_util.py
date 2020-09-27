#!/usr/bin/env python3

import subprocess
import sys
import threading
import warnings

from dataclasses import Field, dataclass, field
from locale import getpreferredencoding
from mmap import mmap
from os import (
    PathLike,
    cpu_count,
    devnull,
    environ as ENV,
    get_terminal_size,
    isatty,
    linesep as NL,
    nice,
    sep as SEP,
    stat_result,
    terminal_size,
    urandom,
)
from pathlib import Path
from subprocess import (
    DEVNULL,
    PIPE,
    STDOUT,
    CalledProcessError,
    CompletedProcess,
    Popen,
    SubprocessError,
    TimeoutExpired,
    call,
    check_call,
    check_output,
    getoutput,
    getstatusoutput,
    list2cmdline,
    run,
)
from sys import (
    argv,
    getdefaultencoding,
    platform as _platform,
    stderr,
    stdout,
    version,
    version_info,
)
from time import monotonic as _time, perf_counter_ns, sleep
from typing import *

from typing_extensions import *

from ._exceptions import *

try:
    import regex as re
except ImportError:
    import re

_debug_: bool = True  # dev mode

WIN32: bool = 'win32' in _platform.lower()
DARWIN: bool = 'darwin' in _platform.lower()

DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or 'utf-8'
DEFAULT_TIMEOUT: float = 15.0


class BasicColors:
    ATTN = '\u001b[38;5;178m'
    BLACK = '\u001b[30m'
    LIGHTBLUE = '\u001b[34m'
    BLUE = '\u001b[38;5;38m'
    CANARY = '\u001b[38;5;226m'
    CHERRY = '\u001b[38;5;124m'
    COOL = '\u001b[38;5;38m'
    CYAN = '\u001b[36m'
    GO = '\u001b[38;5;28m'
    GREEN = '\u001b[32m'
    LIME = '\u001b[32;1m'
    MAGENTA = '\u001b[35m'
    MAIN = '\u001b[38;5;229m'
    PURPLE = '\u001b[38;5;93m'
    RAIN = '\u001b[38;5;93m'
    RED = '\u001b[31m'
    RESET = '\u001b[0m'
    WARN = '\u001b[38;5;203m'
    WHITE = '\u001b[37m'
    YELLOW = '\u001b[33m'


class CompletedProcess1(object):
    """A process that has finished running.

    This is returned by run().

    Attributes:
      args: The list or str args passed to run().
      returncode: The exit code of the process, negative for signals.
      stdout: The standard output (None if not captured).
      stderr: The standard error (None if not captured).
    """

    def __init__(self, args, returncode, stdout=None, stderr=None):
        self.args = args
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __repr__(self):
        args = ['args={!r}'.format(self.args),
                'returncode={!r}'.format(self.returncode)]
        if self.stdout is not None:
            args.append('stdout={!r}'.format(self.stdout))
        if self.stderr is not None:
            args.append('stderr={!r}'.format(self.stderr))
        return '{}({})'.format(type(self).__name__, ', '.join(args))

    def check_returncode(self):
        """Raise CalledProcessError if the exit code is non-zero."""
        if self.returncode:
            raise CalledProcessError(
                self.returncode, self.args, self.stdout, self.stderr)
