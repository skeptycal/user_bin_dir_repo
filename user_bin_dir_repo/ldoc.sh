#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
#*############################################################################
#*  iCloud syncing can take a long time on slow connections and uses
#* 		resources constantly to check and upload changes. This moves
#* 		selected files out of iCloud to a local folder. Careful!
#*
#*	move input files and folders to ~/Docs_local/incoming (out of iCloud)
#*
#*  tested on macOS Big Sur version 11.0 Beta (20A5364e) ; zsh version 5.8
#*	copyright (c) 2019 Michael Treanor
#*	MIT License - https://www.github.com/skeptycal
#*############################################################################
#? ######################## script configuration
	set -a 										# export all
	. $(which ssm) || exit 1					# load standard script modules (ssm)
												# compatibility with 'bash' scripts
	[[ ${SHELL##*/} == 'zsh' ]] && BASH_SOURCE=${(%):-%N} || BASH_SOURCE=${BASH_SOURCE:=$0}
												# 'BASH style' word splitting
	[[ ${SHELL##*/} == 'zsh' ]] && set -o shwordsplit
	path_setup 									# setup path variables (ssm)
	declare -i SET_DEBUG=0						# set to 1+ for verbose testing

#? ######################## constants
CMD=
# OPTIONS='-rlptghiouvCDEH' # rsync options (retain all, verbose, keep links)
# OPTIONS='-uv' # mv options (update only + verbose)
OPTIONS=
SOURCES=
DEST=~/Docs_local/incoming
declare -i USE_RSYNC=1 # set to 1 to use rsync instead of mv

#? ######################## main
main() { # using mv instead of rsync ...
    set_options "$@" # get options and args
	echo

	$CMD $OPTIONS $SOURCES $DEST
}

#? ######################## utilities
die() { echo "${WARN:-}$@" && exit 1; }
set_options() {
    (( $# < 1 )) && die $(usage)

	if [[ "$@" =~ '--rsync' ]]; then
		CMD='rsync'
		USE_RSYNC=1
		# rsync options (retain all, verbose, keep links ...)
		OPTIONS='-ahiuvEH --remove-source-files --delete-after'
		(( SET_DEBUG )) && OPTIONS="-b $OPTIONS" # rsync --dryrun - no changes made
		DEST="$DEST"
	else
		CMD='mv'
		USE_RSYNC=0
		OPTIONS='-fuv' # mv options (update only + verbose)
		(( SET_DEBUG )) && OPTIONS="-b $OPTIONS" # mv backup option - suffix is ~
		DEST="$DEST"
	fi

	if (( SET_DEBUG )); then
		for opt in "$@"; do
			attn "CLI option: $opt"
		done
		echo ""
	fi

    while (( $# > 0 )); do
        case $1 in
            -h|--help)
				help_text
                ;;
            -v|--version)
                die "${SCRIPT_NAME} version ${VERSION}"
                ;;
			--debug)
				SET_DEBUG=1
				;;
			--rsync)
				USE_RSYNC=1
				;;
            -*)
                OPTIONS="${OPTIONS} ${1}"
                ;;
            *)
                SOURCES="${SOURCES}${1} "
                ;;
        esac
        shift
    done
	_debug_show_vars
	}

_debug_show_vars() {
    if (( SET_DEBUG )); then
		_debug_show_paths
		echo ''
		lime "OPTIONS: $OPTIONS"
		lime "SOURCES: $SOURCES"
		lime "   DEST: $DEST"
		echo ''
		blue "SET_DEBUG: $SET_DEBUG"
		blue "USE_RSYNC: $USE_RSYNC"
		echo ''
		lime 'ls SOURCES:'
		green '-----------'
		green $(ls $SOURCES)
    fi
}
#? ######################## documentation
usage() { echo "${GREEN:-}USAGE: ${SCRIPT_NAME##*/}${GREEN:-} [-h|--help] [-v|--version] [--debug] [--rsync] [OPTIONS] FILES...${RESET:-}"; }

help_text() {
	(( USE_RSYNC )) && rsync_help_test || mv_help_text
	exit 0
}

mv_help_text() {
    cat << EOF
Usage: $ [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
  -f, --force                  do not prompt before overwriting
  -i, --interactive            prompt before overwrite
  -n, --no-clobber             do not overwrite an existing file
If you specify more than one of -i, -f, -n, only the final one takes effect.
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 move only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -Z, --context                set SELinux security context of destination
                                 file to default type
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation <https://www.gnu.org/software/coreutils/mv>
or available locally via: info '(coreutils) mv invocation'
EOF
}

rsync_help_text() {
    cat << EOF
rsync  version 2.6.9  protocol version 29
Copyright (C) 1996-2006 by Andrew Tridgell, Wayne Davison, and others.
<http://rsync.samba.org/>
Capabilities: 64-bit files, socketpairs, hard links, symlinks, batchfiles,
    inplace, IPv6, 64-bit system inums, 64-bit internal inums

    rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
    are welcome to redistribute it under certain conditions.  See the GNU
    General Public Licence for details.

    rsync is a file transfer program capable of efficient remote update
    via a fast differencing algorithm.

Usage: 	rsync [OPTION]... SRC [SRC]... DEST
    or 	rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
    or 	rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST
    or 	rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
    or 	rsync [OPTION]... [USER@]HOST:SRC [DEST]
    or 	rsync [OPTION]... [USER@]HOST::SRC [DEST]
    or 	rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
The ':' usages connect via remote shell, while '::' & 'rsync://' usages connect
to an rsync daemon, and require SRC or DEST to start with a module name.

Options
    -v, --verbose               increase verbosity
    -q, --quiet                 suppress non-error messages
        --no-motd               suppress daemon-mode MOTD (see manpage caveat)
    -c, --checksum              skip based on checksum, not mod-time & size
    -a, --archive               archive mode; same as -rlptgoD (no -H)
        --no-OPTION             turn off an implied OPTION (e.g. --no-D)
    -r, --recursive             recurse into directories
    -R, --relative              use relative path names
        --no-implied-dirs       don't send implied dirs with --relative
    -b, --backup                make backups (see --suffix & --backup-dir)
        --backup-dir=DIR        make backups into hierarchy based in DIR
        --suffix=SUFFIX         set backup suffix (default ~ w/o --backup-dir)
    -u, --update                skip files that are newer on the receiver
        --inplace               update destination files in-place (SEE MAN PAGE)
        --append                append data onto shorter files
    -d, --dirs                  transfer directories without recursing
    -l, --links                 copy symlinks as symlinks
    -L, --copy-links            transform symlink into referent file/dir
        --copy-unsafe-links     only "unsafe" symlinks are transformed
        --safe-links            ignore symlinks that point outside the source tree
    -k, --copy-dirlinks         transform symlink to a dir into referent dir
    -K, --keep-dirlinks         treat symlinked dir on receiver as dir
    -H, --hard-links            preserve hard links
    -p, --perms                 preserve permissions
        --executability         preserve the file's executability
        --chmod=CHMOD           affect file and/or directory permissions
    -o, --owner                 preserve owner (super-user only)
    -g, --group                 preserve group
        --devices               preserve device files (super-user only)
        --specials              preserve special files
    -D                          same as --devices --specials
    -t, --times                 preserve times
    -O, --omit-dir-times        omit directories when preserving times
        --super                 receiver attempts super-user activities
    -S, --sparse                handle sparse files efficiently
    -n, --dry-run               show what would have been transferred
    -W, --whole-file            copy files whole (without rsync algorithm)
    -x, --one-file-system       don't cross filesystem boundaries
    -B, --block-size=SIZE       force a fixed checksum block-size
    -e, --rsh=COMMAND           specify the remote shell to use
        --rsync-path=PROGRAM    specify the rsync to run on the remote machine
        --existing              skip creating new files on receiver
        --ignore-existing       skip updating files that already exist on receiver
        --remove-source-files   sender removes synchronized files (non-dirs)
        --del                   an alias for --delete-during
        --delete                delete extraneous files from destination dirs
        --delete-before         receiver deletes before transfer (default)
        --delete-during         receiver deletes during transfer, not before
        --delete-after          receiver deletes after transfer, not before
        --delete-excluded       also delete excluded files from destination dirs
        --ignore-errors         delete even if there are I/O errors
        --force                 force deletion of directories even if not empty
        --max-delete=NUM        don't delete more than NUM files
        --max-size=SIZE         don't transfer any file larger than SIZE
        --min-size=SIZE         don't transfer any file smaller than SIZE
        --partial               keep partially transferred files
        --partial-dir=DIR       put a partially transferred file into DIR
        --delay-updates         put all updated files into place at transfer's end
    -m, --prune-empty-dirs      prune empty directory chains from the file-list
        --numeric-ids           don't map uid/gid values by user/group name
        --timeout=TIME          set I/O timeout in seconds
    -I, --ignore-times          don't skip files that match in size and mod-time
        --size-only             skip files that match in size
        --modify-window=NUM     compare mod-times with reduced accuracy
    -T, --temp-dir=DIR          create temporary files in directory DIR
    -y, --fuzzy                 find similar file for basis if no dest file
        --compare-dest=DIR      also compare destination files relative to DIR
        --copy-dest=DIR         ... and include copies of unchanged files
        --link-dest=DIR         hardlink to files in DIR when unchanged
    -z, --compress              compress file data during the transfer
        --compress-level=NUM    explicitly set compression level
    -C, --cvs-exclude           auto-ignore files the same way CVS does
    -f, --filter=RULE           add a file-filtering RULE
    -F                          same as --filter='dir-merge /.rsync-filter'
                                repeated: --filter='- .rsync-filter'
        --exclude=PATTERN       exclude files matching PATTERN
        --exclude-from=FILE     read exclude patterns from FILE
        --include=PATTERN       don't exclude files matching PATTERN
        --include-from=FILE     read include patterns from FILE
        --files-from=FILE       read list of source-file names from FILE
    -0, --from0                 all *-from/filter files are delimited by 0s
        --address=ADDRESS       bind address for outgoing socket to daemon
        --port=PORT             specify double-colon alternate port number
        --sockopts=OPTIONS      specify custom TCP options
        --blocking-io           use blocking I/O for the remote shell
        --stats                 give some file-transfer stats
    -8, --8-bit-output          leave high-bit chars unescaped in output
    -h, --human-readable        output numbers in a human-readable format
        --progress              show progress during transfer
    -P                          same as --partial --progress
    -i, --itemize-changes       output a change-summary for all updates
        --out-format=FORMAT     output updates using the specified FORMAT
        --log-file=FILE         log what we're doing to the specified FILE
        --log-file-format=FMT   log updates using the specified FMT
        --password-file=FILE    read password from FILE
        --list-only             list the files instead of copying them
        --bwlimit=KBPS          limit I/O bandwidth; KBytes per second
        --write-batch=FILE      write a batched update to FILE
        --only-write-batch=FILE like --write-batch but w/o updating destination
        --read-batch=FILE       read a batched update from FILE
        --protocol=NUM          force an older protocol version to be used
    -E, --extended-attributes   copy extended attributes
        --cache                 disable fcntl(F_NOCACHE)
    -4, --ipv4                  prefer IPv4
    -6, --ipv6                  prefer IPv6
        --version               print version number
    (-h) --help             	show this help (-h works with no other options)

Use "rsync --daemon --help" to see the daemon-mode command-line options.
Please see the rsync(1) and rsyncd.conf(5) man pages for full documentation.
See http://rsync.samba.org/ for updates, bug reports, and answers
EOF
}

main "$@"
