#!/usr/bin/env python3

from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import sys

username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
username = [username, ''][username in [u'loginwindow', None, u'']]
sys.stdout.write(username + '\n')
