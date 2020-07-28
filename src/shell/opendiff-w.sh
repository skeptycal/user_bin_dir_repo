#!/usr/bin/env sh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2016,2086,2230

# Reference: https://www.mercurial-scm.org/wiki/ExtdiffExtension

# opendiff returns immediately, without waiting for FileMerge to exit.
# Piping the output makes opendiff wait for FileMerge.
opendiff "$@" | cat
