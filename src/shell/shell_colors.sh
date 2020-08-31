#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2178,2128,2206,2034

#* ###################### Setup for after 'git clone xxx'

#? ####################### debug
    # SET_DEBUG: set to 1 for verbose testing;
    SET_DEBUG=1

#? ####################### utilities

_set_basic_colors() {
		if [ -t 1 ]; then
			export MAIN="\001\033[38;5;229m"
			export WARN="\001\033[38;5;203m"
			export COOL="\001\033[38;5;38m"
			export BLUE="\001\033[38;5;38m"
			export GO="\001\033[38;5;28m"
			export LIME="\001\033[32;1m"
			export CHERRY="\001\033[38;5;124m"
			export CANARY="\001\033[38;5;226m"
			export ATTN="\001\033[38;5;178m"
			export PURPLE="\001\033[38;5;93m"
			export RAIN="\001\033[38;5;93m"
			export WHITE="\001\033[37m"
			export RESTORE="\001\033[0m\002"
			export RESET="\001\033[0m"
		else
			MAIN=
			WARN=
			COOL=
			BLUE=
			GO=
			LIME=
			CHERRY=
			CANARY=
			ATTN=
			PURPLE=
			RAIN=
			WHITE=
			RESTORE=
			RESET=
		fi
	}

# ssm, standard script modules, is my main shell utilities
# this will either load that OR setup basic colors as needed

color_sample() {
    ce "${MAIN:-}MAIN  ${WARN:-}WARN  ${COOL:-}COOL  ${LIME:-}LIME  ${GO:-}GO  ${CHERRY:-}CHERRY  ${CANARY:-}CANARY  ${ATTN:-}ATTN  ${RAIN:-}RAIN  ${WHITE:-}WHITE  ${RESET:-}RESET"
	}

. $(which ssm) || _set_basic_colors
(( SET_DEBUG == 1 )) && color_sample
