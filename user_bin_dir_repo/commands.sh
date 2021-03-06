#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2155

# use aliases from .zshrc also
setopt aliases

## commands (alias)
## - function command cli adapter
## version 0.0.6 - enable alias expansion for standalone use
##################################################
list-available-commands() { { local function_name ; function_name="${1}" ; local filter_include ; filter_include="${2}" ; }
 echo available commands:
 declare -f \
   | grep -e "^${function_name}" \
   | cut "-f1" "-d " \
   | grep -v -e "which" -e "for-each" -e "payload" -e "initialize" \
   | sed -e "s/${function_name}-//" \
   | xargs -I {} echo "- {}" \
   | sed  "1d" \
   | grep -e "${filter_include}"
}

alias read-command-args='
 list-available-commands ${FUNCNAME}
 echo "enter new command (or q to quit)"
 read command_args
'
alias parse-command-args='
 _car() { echo ${1} ; }
 _cdr() { echo ${@:2} ; }
 _command=$( _car ${command_args} )
 _args=$( _cdr ${command_args} )
'
alias commands='
 #test "${_command}" || { local _command ; _command="${1}" ; }
 #test "${_args}" || { local _args ; _args=${@:2} ; }
 { local _command ; _command="${1}" ; }
 { local _args ; _args=${@:2} ; }
 test ! "$( declare -f ${FUNCNAME}-${_command} )" && {
  {
    test ! "${_command}" || {
     echo "${FUNCNAME} command \"${_command}\" not yet implemented"
    }
    list-available-commands ${FUNCNAME}
  } 1>&2
 true
 } || {
  ${FUNCNAME}-${_command} ${_args}
 }
'
alias run-command='
 {
   commands
 } || true
'
alias handle-command-args='
 case ${command_args} in
   q|quit) {
    break
   } ;;
   *) {
    parse-command-args
   } ;;
 esac
'
alias command-loop='
 while [ ! ]
 do
  run-command
  read-command-args
  handle-command-args
 done
'
##################################################
