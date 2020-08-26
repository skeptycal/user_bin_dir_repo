#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
	# shellcheck shell=bash
	# shellcheck source=/dev/null
	# shellcheck disable=2128


cat << EOF | sed 's/^ *//'
	stuff
EOF

cat <<- EOF | awk 'NR==1 && match($0, /^ +/){n=RLENGTH} {print substr($0, n+1)}'
	stuff
EOF


<<- SO_ANSWER
You can change the here-doc operator to <<-. You can then indent both the here-doc and the delimiter with tabs:

#! /bin/bash
cat <<-EOF
	indented
	EOF
echo Done
Note that you must use tabs, not spaces to indent the here-doc. This means the above example won't work copied (Stack Exchange replaces tabs with spaces). There can not be any quotes around the first EOF delimiter, else parameter expansion, command substitution, and arithmetic expansion are not in effect.

...

Response further down ...

This removes the amount of preceding spaces in the first line from every line in the here document (thanks to anubhava).

# Reference: https://unix.stackexchange.com/a/76483/317591
# anubhava: http://stackoverflow.com/a/33837099/789308

cat <<- EOF | awk 'NR==1 && match($0, /^ +/){n=RLENGTH} {print substr($0, n+1)}'
SO_ANSWER
