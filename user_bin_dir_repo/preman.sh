#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
#? ############################# skeptycal.com

#? preman - open man page in preview
# Reference: https://scriptingosx.com/2017/04/on-viewing-man-pages/

[ -n $1 ] && man -t "$1" | open -f -a "Preview"
