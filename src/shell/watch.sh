#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2178,2128,2206,2034

# Do Over - run a command with args ... over and over and over ...
# it's just quicker and easier than debugging for short scripts
# add compile steps, CI pipeline stuff, logging ... whatever

# similar to https://linux.die.net/man/1/watch
# once I found 'watch' I renamed this script from 'do_over' to 'watch' to be consistent

COUNTER=0 					# not sure why we care how many times it is run ... but i like to see it
SLEEP_INTERVAL=2			# Interval between iterations
SCRIPT_NAME="${0##*/}"		# name of this script
SCRIPT_PATH="${0%/*}"		# path of this script
PID=$$						# PID of this script

while true; do
    "$@"					# literally just running whatever is passed to it
    RETVAL=$?				# not very useful most of the time, but eh ...
    echo "${LIME}<=========================> CTRL-C to STOP the MADNESS <=========================>${RESET:-}"
    echo "${MAIN:-}${SCRIPT_NAME}${CANARY:-} (PID $PID)"
    echo "${GO:-}${SCRIPT_PATH}"
    echo "${CHERRY:-}SLEEP = ${SLEEP_INTERVAL}  ${BLUE:-}COUNT = ${COUNTER}${ATTN:-}  RETVAL = ${RETVAL}${RESET:-}"
    ((COUNTER+=1))
    sleep $SLEEP_INTERVAL
done
