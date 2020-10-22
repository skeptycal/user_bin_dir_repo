#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2230

#?#- ##########################-
    #* repo_clean.sh - remove temporary dev files
    #   build, dist, caches, eggs, tox results
    #* copyright (c) 2019 Michael Treanor
    #* MIT License - https://www.github.com/skeptycal

find . -type d -name "build" -exec rm -rf {} +
find . -type d -name "dist" -exec rm -rf {} +
find . -type d -name ".mypy_cache" -exec rm -rf {} +
find . -type d -name ".pytest_cache" -exec rm -rf {} +
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name "*.egg-info" -exec rm -rf {} +
find . -type d -name ".tox" -exec rm -rf {} +
find . -type f -name "*.py[co]" -exec rm -rf {} +
