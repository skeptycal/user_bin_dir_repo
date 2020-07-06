#!/usr/bin/env python

import subprocess as subp
import os.path
import sys
import re
from collections import defaultdict
from typing import DefaultDict, List


def ps(cmds: List[str] = ["axo", "ppid,pid,comm"]):
    """ #### Return result of shell `ps` command.

        - `cmds`: List - options passed to `ps`
            (default cmds = ['axo', 'ppid,pid,comm'])
        """
    # cmd = ['ps', 'axo', 'ppid,pid,comm'] # original
    cmd: List[str] = ["ps"]
    cmd.extend(cmds)
    print(cmds)
    print(cmd)
    proc: subp.Popen = subp.Popen(cmd, stdout=subp.PIPE)
    proc.stdout.readline()
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
                r"^(\s+\|.+)[\|`](\s+\|- )$", "\g<1> \g<2>", prefix
            )
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
    ps_cmds: List[str] = []
    if len(sys.argv) > 1:  # get cli args ...
        ps_cmds = sys.argv[1:]
    else:  # ... or use defaults
        ps_cmds = ["axo", "ppid,pid,comm"]
    print(f"{ps_cmds=}")

    pidpool: defaultdict = defaultdict(
        lambda: {"cmd": "", "children": [], "ppid": None}
    )

    # parse `ps` output and add values to dictionary
    for ppid, pid, command in ps(ps_cmds):
        ppid = int(ppid)
        pid = int(pid)
        pidpool[pid]["cmd"] = command
        pidpool[pid]["ppid"] = ppid
        pidpool[ppid]["children"].append(pid)

    hieraPrint(pidpool, 1, "")
