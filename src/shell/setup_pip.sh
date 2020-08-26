#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
#* ############################################################################
#* Setup_pip.sh
    #*
    #* Setup pip, git, and python env for use with Python3 and GitHub
    #*
    #* Development Environment:
        #* macOS version 10.15.5 (19F101)
        #* Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
        #*   [Clang 6.0 (clang-600.0.57)]
        #* VSCode Insider's Build (June 2020 version 1.47.0)
        #*
    #* Hardware:
        #* Darwin Kernel Version 19.5.0: Tue May 26 20:41:44 PDT 2020;
        #*   root:xnu-6153.121.2~2/RELEASE_X86_64
        #* Processor: x86_64 i386 (2.2 GHz Quad-Core Intel Core i7)
        #* Machine: MacBookPro11,4 (MacBook Pro (Retina, 15-inch, Mid 2015))
        #* RAM: 16 GB 1600 MHz DDR3; Graphics: Intel Iris Pro 1536 MB
        #*
    #* @author    Michael Treanor  <skeptycal@gmail.com>
    #* @copyright 2020 (c) Michael Treanor
    #* @license   MIT <https://opensource.org/licenses/MIT>
    #* @link      https://www.github.com/skeptycal
    #*
#* ############################################################################
. $(which ssm)
#! DRAFT - this is a work in progress
# exit 0
#? ####################### debug
    # SET_DEBUG: set to 1 for verbose testing;
    SET_DEBUG=1
#? ####################### initialization
    BASH_SOURCE="${0}"
    SCRIPT_NAME="${BASH_SOURCE##*/}"
    SCRIPT_PATH="${BASH_SOURCE%/*}"
    REPO_PATH="$PWD"
    REPO_NAME="${PWD##*/}"
    TEMPLATE_PATH=~/Documents/coding/cc_template

    _debug_show_paths() {
        set -o shwordsplit
        tmp='BASH_SOURCE SCRIPT_NAME SCRIPT_PATH REPO_PATH REPO_NAME TEMPLATE_PATH'
        for i in $tmp; do
            echo -e "${MAIN:-}${(r:15:)i} ... ${CANARY:-}${(P)i}${RESET:-}"
        done;
    }
    dir_list() {
        cd $1
        ls -1Ad */
        cd -
    }

    file_list_color() {
        # list directory contents from path $1 with ansi color codes
        # TODO - work in progress !!
        [ -z $1 ] && { echo "${MAIN:-}$0:${WARN:-} missing path parameter${RESET:-}"; return 1 }
        [[ ${SHELL##*/} == 'zsh' ]] && set -o shwordsplit
        cd $1
        list=$(ls -1A "$1")
        for f in $list; do
            [[ -f $f ]] && echo -e "${GO:-}${f}${RESET:-}";
            [[ -d $f ]] && echo -e "${ATTN:-}${f}${RESET:-}";
        done;
        cd -
    }

    file_list() {
        SEARCH_PATH=${1:-$PWD}
		find $SEARCH_PATH -type f -print
    }
#? ######################## main loop
    _setup_tools() {
        # setup directories:
        mkdir $REPO_NAME
        mkdir bak
        mkdir docs
        mkdir images
        mkdir logs
        mkdir testing

        # setup tools
        git init
        python3 -m venv venv
        source ./venv/bin/activate

        # update pip
        pip install -U pip
        pip install wheel setuptools
        pip install -U wheel setuptools
    } >/dev/null 2>&1

    _copy_files() {
        # using -n - no clobber copy ... nothing overwritten
        [[ ${SHELL##*/} == 'zsh' ]] && set -o shwordsplit
        copy_list=$(file_list $TEMPLATE_PATH)
        for f in $copy_list; do
            cp -n $TEMPLATE_PATH/$f $REPO_PATH;
        done
    }

    _commit_and_status(){
        echo "${CANARY:-}"
        python --version
        echo "${BLUE:-}"
        pip --version
        pipenv install
        git add .
        git commit -m 'initial commit'
        git status
        hub create
    }

    _main_loop(){
        # _debug_show_paths
        echo "setting up repo '$REPO_NAME'"
        _setup_tools "$@"
        echo "copying files ..."
        _copy_files
        echo "initial git commit and upload"
        _commit_and_status

        # run the python portion now ...
        #   or call this from the python script at the start?
    }

#! ######################## entry point
_main_loop "$@"
