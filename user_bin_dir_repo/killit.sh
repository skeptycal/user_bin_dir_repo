#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
	# shellcheck shell=bash
	# shellcheck source=/dev/null
	# shellcheck disable=2230,2086

. $(which ssm)

kill_doc(){
 cat <<- KILL_DOC
 	1	HUP		Hangup: 1
 	2	INT		Interrupt: 2
 	3	QUIT	Quit: 3
 	4	ILL		Illegal instruction: 4
 	5	TRAP	Trace/BPT trap: 5
 	6	ABRT	Abort trap: 6
 	7	EMT		EMT trap: 7
 	8	FPE		Floating point exception: 8
 	9	KILL	Killed: 9
 	10	BUS		Bus error: 10
 	11	SEGV	Segmentation fault: 11
 	12	SYS		Bad system call: 12
 	13	PIPE	Broken pipe: 13
 	14	ALRM	Alarm clock: 14
 	15	TERM	Terminated: 15
 	16	URG		Urgent I/O condition: 16
 	17	STOP	Suspended (signal): 17
 	18	TSTP	Suspended: 18
 	19	CONT	Continued: 19
 	20	CHLD	Child exited: 20
 	21	TTIN	Stopped (tty input): 21
 	22	TTOU	Stopped (tty output): 22
 	23	IO		I/O possible: 23
 	24	XCPU	Cputime limit exceeded: 24
 	25	XFSZ	Filesize limit exceeded: 25
 	26	VTALRM	Virtual timer expired: 26
 	27	PROF	Profiling timer expired: 27
 	28	WINCH	Window size changes: 28
 	29	INFO	Information request: 29
 	30	USR1	User defined signal 1: 30
 	31	USR2	User defined signal 2: 31
KILL_DOC
}

killit_usage() {
	cat <<- KILLIT_USAGE

	Usage: ${LIME:-}killit${RESET:-} [OPTION] [${BLUE:-}SIGNAL${RESET:-}] [${CANARY:-}PID${RESET:-}]

	Usage: ${LIME:-}killit${RESET:-} [-s ${BLUE:-}SIGNAL${RESET:-} | -${BLUE:-}SIGNAL${RESET:-}] ${CANARY:-}PID${RESET:-}...
	  or:  ${LIME:-}killit${RESET:-} -l [${BLUE:-}SIGNAL${RESET:-}]...
	  or:  ${LIME:-}killit${RESET:-} -t [${BLUE:-}SIGNAL${RESET:-}]...
	  or:  ${LIME:-}killit${RESET:-} [--help | --version]

	Send signals to processes, or list signals.

	Mandatory arguments to long options are mandatory for short options too.
	    -s, --signal=${BLUE:-}SIGNAL${RESET:-}, -${BLUE:-}SIGNAL${RESET:-}
		                    specify the name or number of the signal to be sent
	    -l, --list      list signal names, or convert signal names to/from numbers
	    -t, --table     print a table of signal information
	        --help      display this help and exit
	        --version   output version information and exit

	${BLUE:-}SIGNAL${RESET:-} may be a signal name like 'HUP', or a signal number like '1',
	or the exit status of a process terminated by a signal.
	${CANARY:-}PID${RESET:-} is an integer; if negative it identifies a process group.

	${ATTN}NOTE: your shell may have its own version of kill, which usually supersedes
	the version described here.  Please refer to your shell's documentation
	for details about the options it supports.${RESET:-}

	${GO}GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
	Full documentation <https://www.gnu.org/software/coreutils/kill>
	or available locally via: info '(coreutils) kill invocation'${RESET:-}

	${WHITE}************************************************************${RESET}
	'${LIME:-}killit${RESET:-}' ${WHITE}is a wrapper for the GNU coreutils 'gkill' command
	that is often symlinked to 'kill'${RESET:-}

	${GO:-}It allows bypassing of the builtin 'kill' command. While not necessary (simply
	using 'gkill' in place of 'kill' works fine), it was fun to setup.${RESET:-}

	${RAIN:-}copyright (c) 2020 Michael Treanor${RESET:-} (${BLUE:-}http://www.github.com/skeptycal${RESET:-})
	${GO:-}GPL version 3 or any later version${RESET:-}

KILLIT_USAGE
}

killit() {
	KILL=$(which gkill)
	OPT=${1:-}
	SIG=${2:-}
	PID=${3:-}

	case $OPT in
		--help)
			killit_usage
			;;
		--version)
			echo "${LIME:-}killit${RESET:-} version $(gkill --version | head -n 1 | cut -d ' ' -f 4)"
			;;
		-l | --list)
			echo $(kill_doc | grep $SIG'' | cut -d ' ' -f 3 | tr '\n' ' ')
			;;
		-t | -table)
			kill_doc | grep $SIG''
			;;
		-s* | -signal* | -*)
			$($KILL $@)
			;;
		*)
			killit_usage
			;;
	esac
}

killit $@
