#!/usr/bin/env python3

# ? bluetooth.py - originally an aid to fix pairing Google Home on Windows 10

# ? Uses GHLocalAPI - https://rithvikvibhu.github.io/GHLocalApi/
# ? Requires btpair - http://bluetoothinstaller.com/bluetooth-command-line-tools/
# ? Dependency - requests

#  @author Benjamin Gwynn <me@benjamingwynn.com>

import ctypes
import os
from platform import platform
from subprocess import check_output, PIPE, STDOUT
import sys

# pip install requests (or pipenv if you're into that kind of thing)
import requests

IS_WIN: bool = 'windows' in platform().lower()


def shell(args: str):
    cmd = tuple(args.split())
    return str(check_output(cmd, shell=True, stderr=STDOUT))


if IS_WIN:
    def is_admin():
        # more code copied from stack overflow https://stackoverflow.com/a/56022769
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
else:
    def is_admin():
        cmd = 'arp -a | findstr "' + macstr + '" '
        try:
            return shell(cmd)
        except:
            return False


def find_ip(mac):
    # apparently you can't use ':', you have to use '-' for ARP, la dee da.
    macstr = mac.replace(':', '-')
    cmd = 'arp -a | findstr "' + macstr + '" '
    returned_output = shell(cmd)
    parse = str(returned_output).split(' ', 1)
    ip = parse[1].split(' ')
    return ip[1]


def get_ips():
    cmd = 'arp -a'
    retval = str(subprocess.check_output(
        (cmd), shell=True, stderr=subprocess.STDOUT))

    retval.replace('?', '')

    return retval


ips = get_ips()
print(type(ips))
print()
print(ips)

# ? -------------------------------> original code for Windows 10
# # spit out usage errors
# if (sys.argv.count < 2):
#     print("usage " + sys.argv[0] + " <google home mac address>")
#     print("- you can find the mac address on the bottom of the device settings on the Google Home app")
#     exit(1)

# # lower case is important for correct ARP lookup in find_ip.
# mac = sys.argv[1].lower()
# print("Google Home MAC Address: " + mac)
# ip = find_ip(mac)
# print("Google Home IP: " + ip)

# if is_admin():
#     # btpair requires admin.
#     print("Hey, you're an admin, that's great!")
#     print("Unpairing Windows Bluetooth devices...")
#     # why not btpair -u with a specific mac? because it doesn't work, try it.
#     os.system("btpair -u")
# else:
#     print("\n!! You must be an admin to run this script!\n\n* Why? The btpair program needs it to unpair devices RELIABLY, unlike Control Panel which always does so at user-level, causing devices to get stuck. Please check the source code before running this as an admin to ensure it has not been tampered with.\n")
#     exit(1)

# # this is done using https://rithvikvibhu.github.io/GHLocalApi/#bluetooth-bluetooth-bond-post
# print("Forgetting paired devices on Google Home...")
# requests.post("http://" + ip + ":8008/setup/bluetooth/bond",
#               headers={"Content-Type": "application/json"})

# print("Setting Google Home to discoverable...")
# requests.post("http://" + ip + ":8008/setup/bluetooth/discovery",
#               headers={"Content-Type": "application/json"})

# print("Trying to use btpair to connect, this NEVER works for me, but might for you...")
# os.system("btpair -p -b " + mac)

# print("Opening the legacy Bluetooth panel (fun-fact: you can close this panel after the device starts to install!)")
# os.system("DevicePairingWizard.exe")
