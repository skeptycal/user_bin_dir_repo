#!/usr/bin/env zsh
# -*- coding: utf-8 -*-

. $(which ssm)

export speedlog_file=~/.speedtest.csv

me "speedlog - continuously run speedtest once per minute"
me "  create a log of download speeds at $(realpath $speedlog_file)"while true; do
	speedtest --format=csv >>$speedlog_file
	cat $speedlog_file | tail -n 1
done
