#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2128
##############################################################################
#   options.sh - handle command line options in zsh and bash scripts
#
#   OPTIONS
#       --version   - display version information
#       --help      - display help information
#       --npm       - fix common node / npm permissions issue
#
# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal
###############################################################################

#TODO --- stuff


###############################################################################
# Based on 'Advanced Bash-Scripting Guide: Appendix G. Command-Line Options'
# Reference: https://www.tldp.org/LDP/abs/html/standard-options.html
#
# G.1. Standard Command-Line Options
# Over time, there has evolved a loose standard for the meanings of command-line option flags. The GNU utilities conform more closely to this "standard" than older UNIX utilities.

# Traditionally, UNIX command-line options consist of a dash, followed by one or more lowercase letters. The GNU utilities added a double-dash, followed by a complete word or compound word.

# The two most widely-accepted options are:

# -h

# --help

# Help: Give usage message and exit.

# -v

# --version

# Version: Show program version and exit.

# Other common options are:

# -a

# --all

# All: show all information or operate on all arguments.

# -l

# --list

# List: list files or arguments without taking other action.

# -o

# Output filename

# -q

# --quiet

# Quiet: suppress stdout.

# -r

# -R

# --recursive

# Recursive: Operate recursively (down directory tree).

# -v

# --verbose

# Verbose: output additional information to stdout or stderr.

# -z

# --compress

# Compress: apply compression (usually gzip).

# However:

# In tar and gawk:

# -f

# --file

# File: filename follows.

# In cp, mv, rm:

# -f

# --force

# Force: force overwrite of target file(s).

# Caution
# Many UNIX and Linux utilities deviate from this "standard," so it is dangerous to assume that a given option will behave in a standard way. Always check the man page for the command in question when in doubt.

# A complete table of recommended options for the GNU utilities is available at the GNU standards page.
