#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2178,2128,2206,2034

#* ###################### Setup User ~/bin directory repo
#*

#? ######################## configuration
    export YEAR=$(date "+%Y")
    t0=$(date "+%s.%n")

    cleanup() {
        # cleanup and exit script
        unset echo

        # calculate and display script time
        t1=$(date "+%s.%n")
        dt=$((t1-t0))
        printf '\n%bScript %s took %.3f seconds to load.\n\n' "${GO:-}" "$0" "$dt"
        unset t0 t1 dt
    }

    trap cleanup EXIT

    # more portable alternative
    echo () {
        if [ -n "$1" ]; then
            printf '%s' "$1"
            shift
        fi
        for arg in "$@"; do
            printf ' %s' "$arg"
        done
        printf '%s\n' ''
    }

    exists() { type $1 > /dev/null 2>&1 ; }

    _set_basic_colors() {
        declare -x MAIN && MAIN=$(echo -en '\001\033[38;5;229m')
        declare -x WARN && WARN=$(echo -en '\001\033[38;5;203m')
        declare -x COOL && COOL=$(echo -en '\001\033[38;5;38m')
        declare -x BLUE && BLUE=$(echo -en '\001\033[38;5;38m')
        declare -x GO && GO=$(echo -en '\001\033[38;5;28m')
        declare -x LIME && LIME=$(echo -en '\001\033[32;1m')
        declare -x CHERRY && CHERRY=$(echo -en '\001\033[38;5;124m')
        declare -x CANARY && CANARY=$(echo -en '\001\033[38;5;226m')
        declare -x ATTN && ATTN=$(echo -en '\001\033[38;5;178m')
        declare -x PURPLE && PURPLE=$(echo -en '\001\033[38;5;93m')
        declare -x RAIN && RAIN=$(echo -en '\001\033[38;5;93m')
        declare -x WHITE && WHITE=$(echo -en '\001\033[37m')
        declare -x RESTORE && RESTORE=$(echo -en '\001\033[0m\002')
        declare -x RESET && RESET=$(echo -en '\001\033[0m')
    }

    # ssm - standard script modules or alternate
    . "$(command -v ssm)" > /dev/null 2>&1 || _set_basic_colors

#? ######################## setup
    _setup_brew() {
        exists brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

        brew cleanup
        brew doctor
        brew update

        brew install git hub gpg python@3.8 poetry pre-commit

    } # > /dev/null 2>&1

    main() {

        [ ! -d ~/bin ] && mkdir ~/bin

        [ "$1" == '--nobrew' ] && echo 'Skipping HomeBrew install ...' || _setup_brew

        # add ~/bin to PATH
        case ${SHELL##*/} in
            zsh)
                export PATH=$PATH:~/bin
                echo 'export PATH=$PATH:~/bin'  >> ~/.zshrc
                ;;
            bash)
                export PATH=$PATH:~/bin
                echo 'export PATH=$PATH:~/bin'  >> ~/.bash_profile
                ;;
            *csh)
                set path = ($path ~/bin)
                echo 'set path = ($path ~/bin)'  >> ~/.cshrc
                ;;
            *) # including ksh, sh
                export PATH=$PATH:~/bin
                echo 'export PATH=$PATH:~/bin'  >> ~/.profile
                ;;
        esac

        #initialize ~/bin/binit
        src/shell/binit.sh src/shell/binit.sh

        repo_path=$PWD
        repo_name=${PWD##*/}

        mkdir $repo_name
        git init
        python3 -m venv venv

        binit
        BINS=( src/go/brightness src/go/darkmode do_over git_gpg gitit log_urls parse_tags ptags pycache_remove repo_clean speedtest ssm ssm_constants ssm_debug ssm_usage src/tree-1.5.3/tree )

        _setup_prereqs

        REQS=
        DEV_REQS=( pip wheel setuptools pylint pytest tox coverage pytest-cov )
        DEV_OPTS=( flake8 black tox-travis Sphinx sphinx-autobuild sphinx-rtd-theme )

        _setup_reqs

        _end_timer
    }

main "$@"

# continue setup in python
python3 -m setup


#? ${PATH//:/\\n}    - replace all colons with newlines to display as a list
#? ${PATH// /}       - strip all spaces
#? ${VAR##*/}        - return only final element in path (program name)
#? ${VAR%/*}         - return only path elements in path (without program name)
