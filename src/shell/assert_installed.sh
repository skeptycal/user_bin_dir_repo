#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2128

exists() { type $1 > /dev/null 2&>1 ; }

assert_installed() {
    for var in "$@"; do
        if ! type $var &> /dev/null; then
            echo "{WARN:-}Install ${var}!"
            exit 1
        fi
    done
}
