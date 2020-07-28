#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2230

#?#- ##########################-
#* bc_remove.sh - remove python bytecode cache files and directories
#* copyright (c) 2019 Michael Treanor
#* MIT License - https://www.github.com/skeptycal

# inherit SET_DEBUG; default 0; set to 1 for verbose testing
SET_DEBUG=${SET_DEBUG:-0}

sudo find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
