#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2128,2206,2034
#? ################# .zshrc - main config for macOS with zsh ###############
 #* copyright (c) 2019 Michael Treanor     -----     MIT License
 #? ###################### https://www.github.com/skeptycal ##################

 #* number of years the first commercial
 #*   modem would take to transmit a movie: 42.251651342415241
 #*   this is very nearly the time since I wrote my first program
 #*   I'm glad I didn't watch that movie instead ...

#? ###################### copyright (c) 2019 Michael Treanor #################

presuf() {
		usage="${WHITE:-}usage: ${LIME:-}presuf ${GREEN:-}[--help|--verbose] [--force] [--autoname] [--pattern PATTERN] [--prefix PREFIX] [--suffix SUFFIX]${RESET:-}"

		verbose=0				# display details
		force=0					# force changes (default is dry-run)
		auto=0					# autonumber suffixes
		count=1					# starting number for autonumbering

		pattern= 				# default pattern is * but is supplied later ...
		prefix=				 	# default prefix is parent directory name + underscore
		suffix=					# default suffix is none (meaning leave it unchanged)

		vb () { (( verbose )) && blue "$@"; }

		while [[ $# > 0 ]]; do
			case $1 in
				-h|--help)
					me $usage
					return 0
					;;
				-a|--autonumber)
					auto=1
					shift
					;;
				-f|--force)
					force=1
					shift
					;;
				-v|--verbose)
					verbose=1
					vb "verbose detail output is on"
					shift
					;;
				--pattern)
					shift
					pattern="$1"
					shift
					;;
				-p|--prefix)
					shift
					prefix="$1"
					shift
					;;
				-s|--suffix)
					shift
					suffix="$1"
					shift
					;;
				*)
					shift
					;;
			esac
		done

		if (( auto )); then
			if [ -z $prefix ]; then
				prefix="${PWD##*/}_"
				vb "auto-prefix: $prefix"
			fi
		fi

		vb "verbose: $verbose"
		vb "force: $force"
		vb "auto: $auto"
		vb "pattern: $pattern"
		vb "prefix: $prefix"
		vb "suffix: $suffix"
		vb ""
		vb "${LIME:-}Processing ..."
		vb "----------------------"

		for f in ${pattern:-*}; do

			if [[ -z $suffix ]]; then
				fmt="${prefix:-}${f}"
			else
				if (( auto )); then
					printf -v autosuf '_%05d' $count
					fmt="${prefix:-}${f%%.*}.${suffix}"
			fi
			vb "$fmt"
			(( force > 0 )) && mv $f ${1:-}${f##*.}${2:-}
		done
	}

if (( $# > 0 ))
presuf "$@"
