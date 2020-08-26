#!/usr/bin/env python

import subprocess as subp
import os.path
import sys
import re
from collections import defaultdict
from typing import DefaultDict, List

if True:
    LOGURU_LEVEL = 'TRACE'
    from loguru import logger


def ps(cmds: List[str] = ["axo", "ppid,pid,comm"]):
    """ #### Return result of shell `ps` command.

        - `cmds`: List - options passed to `ps`
            (default cmds = ['axo', 'ppid,pid,comm'])
        """
    # cmd = ['ps', 'axo', 'ppid,pid,comm'] # original
    cmd: List[str] = ["ps"]
    cmd.extend(cmds)
    proc: subp.Popen = subp.Popen(cmd, stdout=subp.PIPE)
    proc.stdout.readlines()
    for line in proc.stdout:
        yield line.rstrip().split(None, 2)


def hieraPrint(pidpool, pid, prefix=""):
    pname: str = ""
    if os.path.exists(pidpool[pid]["cmd"]):
        pname = os.path.basename(pidpool[pid]["cmd"])
    else:
        pname = pidpool[pid]["cmd"]
    ppid = pidpool[pid]["ppid"]
    pppid = pidpool[ppid]["ppid"]
    try:
        if pidpool[pppid]["children"][-1] == ppid:
            prefix = re.sub(
                r"^(\s+\|.+)[\|`](\s+\|- )$", "\g<1> \g<2>", prefix)
    except IndexError:
        pass
    try:
        if pidpool[ppid]["children"][-1] == pid:
            prefix = re.sub(r"\|- $", "`- ", prefix)
    except IndexError:
        pass
    # sys.stdout.write('{0}{1}({2}){3}'.format(prefix, pname, pid, os.linesep))
    print("{0}{1}({2}){3}".format(prefix, pname, pid, ""), file=sys.stdout)
    if len(pidpool[pid]["children"]):
        prefix = prefix.replace("-", " ")
        for idx, spid in enumerate(pidpool[pid]["children"]):
            hieraPrint(pidpool, spid, prefix + " |- ")


if __name__ == "__main__":
    args: List[str] = ["axo", "ppid,pid,comm"]
    if len(sys.argv) > 1:  # get cli args ...
        args = sys.argv[1:]

    logger.trace(f"{args=}")

    pidpool: defaultdict = defaultdict(
        lambda: {"cmd": "", "children": [], "ppid": None}
    )

    # parse `ps` output and add values to dictionary
    print('# parse `ps` output and add values to dictionary')
    for ppid, pid, command in ps(args):
        ppid = int(ppid)
        pid = int(pid)
        pidpool[pid]["cmd"] = command
        pidpool[pid]["ppid"] = ppid
        pidpool[ppid]["children"].append(pid)

    hieraPrint(pidpool, 1, "")
