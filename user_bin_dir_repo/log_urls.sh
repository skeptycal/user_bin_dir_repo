#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2016,2086,2230

. $(which ssm)
PREVIOUS_URL=''
hidden='' # leave blank for visible output ...

# getopt --test >/dev/null
# if [[ $? != 4 ]]; then
#     attn "I'm sorry, `getopt --test` failed in this environment."
#     rain 'On macOS, install with `brew install gnu-getopt`'
#     br
# else
exec 1>&2

getURL() {
    # copy URL from active tab of Google Chrome to macOS clipboard
    if [[ $OS = 'darwin' ]]; then
        # set <url> to active Chrome tab url
        url=$(osascript -e 'tell application "Google Chrome" to return URL of active tab of front window')

        # copy to clipboard
        printf "%s" "$url" | pbcopy

        # -v is verbose : if -v ... print url to stdout in addition
        [ "$1" = '-q' ] || printf "%s\n" "$url"
    fi
    }

ping_avg() {
    usage="$0 [-h] | [COUNT URL]"
    # attn "$0 $1 $2"
    case $1 in
        '-h'|'--help'|'help')
            me $usage
            exit
            ;;
        *)
            # extract the average ping time (ms) from 'ping' output
            # $1 = number of pings to average
            count=$1

            # $2 = url to test
            # remove schema and folders
            url_short=$(echo "$2" | cut -d '/' -f 3)

            # ww
            ping -c "$count" "$url_short" | tail -n 1 | cut -d '/' -f 6
            ;;
    esac
    }

hide(){ attn "hidden $@"; } #! debug feature

log_urls() {
    log_urls_usage="$0 [SLEEP_TIME] [COUNT] [URL_LOG_FILENAME] [HIDDEN]"
    # time to sleep between checks						sq- default 10s
    # number of repeats for average ping measurement	- default 3
    # location of log file								 - default ~/.url_log.log
    # hidden flag										 - default True

    if [ "$1" = '-h' ] || [ "$1" = '--help' ] || [ "$#" -lt 1 ]; then
        hide "Usage: $log_urls_usage"
    else
        sleep_time=${1:-10}                       #! default 1 for testing
        count=${2:-3}
        url_log=${3:-~/.log_urls.log}
        hidden=${4:-$hidden}

        # choose comparison site (set blank to skip the speed comparison)
        comp=''
        # comp="www.example.com"
        # comp="www.google.com"
        # comp="192.168.1.100"
        # comp="skeptycal.com"

        # display config ...
        [[ -z $hidden ]] && me "$0 Configuration: # of args: $# -- logging: sleep = $sleep_time count = $count logfile = $url_log" || hide config

        # shellcheck disable=SC2078 # ignore constant expression  `while [ : ]`
        while [ : ]
        do
            # get url of Chrome active tab
            url=$(osascript -e 'tell application "Google Chrome" to return URL of active tab of front window')

            # remove schema and folders
            url_short=$(echo "$url" | cut -d '/' -f 3)

            # get average ping of url - may interfere with forms or secure websites ...
            test_avg=$(ping_avg $count $url)

            [[ -n $comp ]] && comp_avg=$(ping_avg $count $comp)

            #TODO - check if url = PREVIOUS_URL ... to keep down the spam
            if [[ $url = "$PREVIOUS_URL" ]]; then
                true #TODO do stuff if $url is the same ...
            else
                [[ -z $hidden ]] && canary "$(date), $url, ${test_avg}, ${comp_avg}" || hide
                PREVIOUS_URL=$url
            fi

            # log to $url_log - the logging to file is always active, even if screen output is hidden
            printf "%s\n" "$(date), $url, $test_avg, ${comp_avg:='no comparison'}" >>$url_log

            sleep $sleep_time
        done
    fi
}

# log_urls $@
