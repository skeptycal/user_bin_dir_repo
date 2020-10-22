#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2178,2128,2206,2034

# Fix python 3.6 - 3.9 building on macOS 20 (Big Sur)
	# This is a patch I use until the committee merges the official PR into the
	# builds for 3.6 - 3.9

# Notes from CPython GitHub Repo
	# "This PR is needed to build on macOS 11, because the release of Darwin is now
	# 20.0.0, which doesn't match any of the Darwin cases used to disable
	# _POSIX_C_SOURCE on macOS."

#? ######################## environment

	# load personal utilities and themes -- or basic ansi colors
	. $(which ssm) || . $(which ansi_colors)

	# 'BASH style' word splitting
	[[ ${SHELL##*/} == 'zsh' ]] && set -o shwordsplit

#? ######################## debug
    # SET_DEBUG: set to 1 for dry-run testing;
    SET_DEBUG=1
	(( SET_DEBUG=1 )) && set +n

    _debug_show_paths() {
        tmp='BASH_SOURCE SCRIPT_NAME SCRIPT_PATH REPO_PATH REPO_NAME'
        for i in $tmp; do
            echo "${MAIN:-}${(r:15:)i} ... ${CANARY:-}${(P)i}${RESET:-}"
        done;
    	}
#? ######################## configuration

	ms() { echo $(($(gdate +%s%0N)/1000000)) }
	t0=$(ms)
    cleanup() {
        # cleanup and exit script

        # calculate and display script time
        dt=$(( $(ms)-t0 ))
		printf '\n%b %d %b\n\n' "${GREEN:-}Script ${SCRIPT_NAME} took" ${dt} "ms to load.${RESET:-}"
        unset t0 dt
    	}
    trap cleanup EXIT

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

	VERSION="${ATTN:-}0.1.0${RESET:-}"

    BASH_SOURCE=$(realpath "${0}")
    SCRIPT_NAME="${BLUE:-}${BASH_SOURCE##*/}${RESET:-}"
    SCRIPT_PATH="${CANARY:-}${BASH_SOURCE%/*}${RESET:-}"

    REPO_PATH="${LIME:-}$(realpath $PWD)${RESET:-}"
    REPO_NAME="${LIME:-}${REPO_PATH##*/}${RESET:-}"

#? ######################## utilities
	dbecho() { (( SET_DEBUG==1 )) && echo "${ATTN:-}$@"; }
	die() { echo "${WARN:-}$@" && exit 1; }
	is_empty() { [ -z "$(ls -A $1)" ]; }
    exists() { command -v $1 > /dev/null 2>&1 ; }
	_setup_brew() {
		if (( $SET_DEBUG == 1 )); then
			echo "${ATTN:-}Install brew if it is not installed... not done in debug mode."
		else
        	exists brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

			brew cleanup
			brew doctor
			brew update

			brew install gcc zlib
			brew upgrade gcc zlib

			brew cleanup
			brew doctor
		fi
	}  > /dev/null 2>&1

#? ######################## main
	usage() {
		echo "${GREEN:-}USAGE: ${SCRIPT_NAME} ${GREEN:-}[-h|--help][-v|--version][--dry-run][--patch]${RESET:-}"
		echo ""
		echo "${GREEN:-}OPTIONS:${RESET:-}"
		echo "  Use (with '--patch' parameter) to patch and install python"
		echo "  install from source (versions 3.6 to 3.9)"
	}
	make_install() {
		# in the event that zlib is not cooperating ... hey, it works ...
		# I am an amateur so this is the best I could do on this part ...
		# https://github.com/netdata/netdata/issues/24
		# https://gcc.gnu.org/install/configure.html
		if $(command -v zlib); then
			./configure --enable-optimizations
		else
			./configure ZLIB_CFLAGS=" " ZLIB_LIBS="-lz" --enable-optimizations
		fi


		SIGNATURE="  # NOTE (github.com/skeptycal) "
		COMMENT="changed per https://github.com/python/cpython/pull/21113/files"



		SOURCEFILE=./configure.test
		TARGET="  Darwin/1[0-9].*)"
		REPLACEMENT="  Darwin/[12][0-9].*)"
		COMMENT="- changed per https://github.com/python/cpython/pull/21113/files"

		cp $SOURCEFILE $SOURCEFILE.tmp
		sed -i "//${TARGET}//${REPLACEMENT}" ${SOURCEFILE}


		TARGET="  Darwin/1@<:@0-9@:>@.*)"
		REPLACEMENT="  Darwin/@<:@[12]@:>@@<:@0-9@:>@.*)"
		COMMENT="- changed per https://github.com/python/cpython/pull/21113/files"


		# Default was 11.0 but that failed during 'make altinstall' for python 3.6
		# MACOSX_DEPLOYMENT_TARGET=10.6 is the long-time combatibility version
		# https://stackoverflow.com/questions/33184316/os-x-python-can-i-explicitly-set-macosx-deployment-target-for-extensions
		# MACOSX_DEPLOYMENT_TARGET=10.6
		# export MACOSX_DEPLOYMENT_TARGET
		# make altinstall did not work with any setting I tried
		# fix the aliases manually later and install preferred version last

		# -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include
		CFLAGS='-I/usr/local/readline/include -I/usr/local/zlib/include -I/usr/local/openssl/include'
		LDFLAGS='-L/usr/local/readline/lib -L/usr/local/openssl/lib -L/usr/local/zlib/lib'

		/bin/sh ./configure

		CFLAGS="-I$(brew --prefix readline)/include -I$(brew --prefix openssl)/include -I$(xcrun --show-sdk-path)/usr/include"
		LDFLAGS="-L$(brew --prefix readline)/lib -L$(brew --prefix openssl)/lib"
		PYTHON_CONFIGURE_OPTS=--enable-unicode=ucs2
		pyenv install -v 3.6.0


		make profile-opt
		make test
		make altinstall
		make testall
		make install
		make frameworkinstall
	}

	set_options() {
		(( $# < 2 )) && die $(usage)
		while (( $# > 0 )); do
			case $1 in
				-h|--help)
					usage
					exit 0
					;;
				-v|--version)
					echo "${SCRIPT_NAME} version ${VERSION}"
					exit 0
					;;
				--dry-run)
					echo "${SCRIPT_NAME} in ${ATTN:-}'--dry-run'${RESET:-} mode ${GREEN:-}(only show commands ... do nothing)${RESET:-}"
					DEBUG=1
					set +n
					shift
					;;
				--patch)
					echo "${MAIN:-}Performing patch and install from source for python in ${REPO_NAME}."
					echo ""
					;;
			esac
		done
		}

main() {
	(( SET_DEBUG==1 )) && _debug_show_paths
	set_options "$@"
	_setup_brew
	# make_install
}

main "$@"


# This is the notice from python 3.6.10 (Makefile)

	# Generated automatically from Makefile.pre by makesetup.
	# Top-level Makefile for Python
	#
	# As distributed, this file is called Makefile.pre.in; it is processed
	# into the real Makefile by running the script ./configure, which
	# replaces things like @spam@ with values appropriate for your system.
	# This means that if you edit Makefile, your changes get lost the next
	# time you run the configure script.  Ideally, you can do:
	#
	#	./configure
	#	make
	#	make test
	#	make install
	#
	# If you have a previous version of Python installed that you don't
	# want to overwrite, you can use "make altinstall" instead of "make
	# install".  Refer to the "Installing" section in the README file for
	# additional details.
	#
	# See also the section "Build instructions" in the README file.
