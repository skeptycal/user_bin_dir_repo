#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2128

#? ############################# skeptycal.com
#? binit - create symbolic links to [FILE(s)] in the current user's ~/bin folder
# using GNU coreutils: <https://www.gnu.org/software/coreutils/>

# import standard script modules, if available
. $(which ssm) >/dev/null 2>&1

# BASH_SOURCE="${0}"
# SCRIPT_NAME="${BASH_SOURCE##*/}"
# SCRIPT_PATH="${BASH_SOURCE%/*}"

# list of cli arguments passed, including FILES to link
ARGS=( ${@:1} )


# if no files are given, echo usage information and exit
if [ -z "$ARGS" ]; then
    echo " ${CANARY:-}${BOLD:-}$ME${RESET:-} - create symbolic links for ${GO:-}FILE(s)${RESET:-} in ${BLUE:-}~/bin${RESET:-}"
    echo "    ${MAIN:-}Usage: ${CANARY:-}$ME ${GO:-}FILES(s)${RESET:-}"
    return 1
fi

# prefer hard links; backups performed for files that are overwritten
# remove extensions for sh and py files ... personal preference
for arg in $ARGS; do
    src=$(realpath $arg)
    if [ -r $src ]; then
        chmod a+x $src

        tgt=${src##*/}
        tgt=${tgt%.sh*}
        tgt=${tgt%.py*}
        tgt=${tgt%.php*}
        tgt=~/bin/$tgt

        ln -bv $src $tgt

        # if hardlink didn't work, try symbolic link
        if ! [ -r $tgt ]; then
            ln -sbv $src $tgt
        fi


    else
        exit "${arg} (${src}) is not readable."
    fi
done

# $SHELL -l
