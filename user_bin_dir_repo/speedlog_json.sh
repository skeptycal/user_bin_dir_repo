#!/usr/bin/env zsh
# -*- coding: utf-8 -*-

. $(which ssm)

export speedlog_json_file=~/.speedtest.json

me "speedlog_json - continuously run speedtest once per minute"
me "  create a log of download speeds at $(realpath $speedlog_json_file)"
while true; do
	speedtest --format=json >>$speedlog_json_file
	cat $speedlog_json_file | tail -n 1
done
