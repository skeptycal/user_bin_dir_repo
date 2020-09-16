#!/usr/bin/env python3

from dataclasses import dataclass
from os import PathLike, walk


class QuotingStyleFormats:
    '-N' = 'print entry names without quoting'
    '--literal' = 'print entry names without quoting'
    '-b' = 'print C-style escapes for nongraphic characters'
    '--escape' = 'print C-style escapes for nongraphic characters'
    '-q' = 'print ? instead of nongraphic characters'
    '--hide-control-chars' = 'print ? instead of nongraphic characters'
    '--show-control-chars' = 'show nongraphic characters as-is (the default, unless program is "ls" and output is a terminal)'
    '-Q' = 'enclose entry names in double quotes'
    '--quote-name' = 'enclose entry names in double quotes'
    '--quoting-style = WORD' = 'use quoting style WORD for entry names: literal, locale, shell, shell-always, shell-escape, shell-escape-always, c, escape (overrides QUOTING_STYLE environment variable)'


@dataclass
class LS:
    path_name: PathLike = ''
    formatstr: str = ''
    sort: str = 'a'
    options = 'laFg'
    links: str = ''  # HLD
    escape: bool = False
    QUOTING_STYLE: QuotingStyleFormats = QuotingStyleFormats.N

    """
        Usage: gls [OPTION]... [FILE]...

        List information about the FILEs (the current directory by default).
        Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

        Mandatory arguments to long options are mandatory for short options too.

        The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
        Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
        Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

        The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
        FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
        then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
        TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
        Also the TIME_STYLE environment variable sets the default style to use.

        Using color to distinguish file types is disabled both by default and
        with --color=never.  With --color=auto, ls emits color codes only when
        standard output is connected to a terminal.  The LS_COLORS environment
        variable can change the settings.  Use the dircolors command to set it.

        Exit status:
        0  if OK,
        1  if minor problems (e.g., cannot access subdirectory),
        2  if serious trouble (e.g., cannot access command-line argument).

        GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
        Full documentation <https://www.gnu.org/software/coreutils/ls>
        or available locally via: info '(coreutils) ls invocation'

        """

    def links_ls():
        """
        -H, --dereference-command-line
                                    follow symbolic links listed on the command line
            --dereference-command-line-symlink-to-dir
                                    follow each command line symbolic link
                                    that points to a directory
        -L, --dereference           when showing file information for a symbolic
                                    link, show information for the file the link
                                    references rather than for the link itself
            """

    def special_ls():
        """
        --color[=WHEN]              colorize the output; WHEN can be 'always' (default
                                    if omitted), 'auto', or 'never'; more info below
        -D, --dired                 generate output designed for Emacs' dired mode
            --hyperlink[=WHEN]      hyperlink file names; WHEN can be 'always'
                                    (default if omitted), 'auto', or 'never'
        -R, --recursive             list subdirectories recursively
        --help                      display this help and exit
        --version                   output version information and exit
        -1                          list one file per line.  Avoid '\n' with -q or -b
        """

    def formatls():
        """
        QUOTING_STYLE:
        -N, --literal               print entry names without quoting
        -b, --escape                print C-style escapes for nongraphic characters
        -q, --hide-control-chars    print ? instead of nongraphic characters
            --show-control-chars    show nongraphic characters as-is (the default,
                                    unless program is 'ls' and output is a terminal)
        -Q, --quote-name            enclose entry names in double quotes
            --quoting-style=WORD    use quoting style WORD for entry names:
                                    literal, locale, shell, shell-always,
                                    shell-escape, shell-escape-always, c, escape
                                    (overrides QUOTING_STYLE environment variable)




        columns formatting:
        -C                          list entries by columns
        -T, --tabsize=COLS          assume tab stops at each COLS instead of 8
        -x                          list entries by lines instead of by columns
        -w, --width=COLS            set output width to COLS.  0 means no limit



        size formatting:
        -k, --kibibytes             default to 1024-byte blocks for disk usage;
                                    used only with -s and per directory totals
        --block-size=SIZE           with -l, scale sizes by SIZE when printing them;
                                    e.g., '--block-size=M'; see SIZE format below
        -h, --human-readable        with -l and -s, print sizes like 1K 234M 2G etc.
        -s, --size                  print the allocated size of each file, in blocks
        --si                        likewise, but use powers of 1000 not 1024



        classification formatting:
        -p, --indicator-style=slash
                                    append / indicator to directories
        -F, --classify              append indicator (one of */=>@|) to entries
            --file-type             likewise, except do not append '*'
            --format=WORD           across -x, commas -m, horizontal -x, long -l,
                                    single-column -1, verbose -l, vertical -C

            --indicator-style=WORD  append indicator with style WORD to entry names:
                                    none (default), slash (-p),
                                    file-type (--file-type), classify (-F)


        """

    def show_ls():
        """ show = one of

        -a, --all                  do not ignore entries starting with .
        -A, --almost-all           do not list implied . and ..
            --author               with -l, print the author of each file
        -B, --ignore-backups       do not list implied entries ending with ~
        -d, --directory            list directories themselves, not their contents
        -g                         like -l, but do not list owner
            --full-time            like -l --time-style=full-iso
        -G, --no-group             in a long listing, don't print group names
        -i, --inode                print the index number of each file
        --hide=PATTERN             do not list implied entries matching shell PATTERN
                                   (overridden by -a or -A)
        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
        -l                         use a long listing format
        -m                         fill width with a comma separated list of entries
        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
        -o                         like -l, but do not list group information
        -Z, --context              print any security context of each file
            """

    def sortls():
        """ sort = one of cftuvSUX

            -r, --reverse              	reverse order while sorting

            --group-directories-first
                                    group directories before files;
                                    can be augmented with a --sort option, but any
                                    use of --sort=none (-U) disables grouping


            none						alphabetically
            -c                         	with -lt: sort by, and show, ctime (time of last
                                        modification of file status information);
                                        with -l: show ctime and sort by name;
                                        otherwise: sort by ctime, newest first
            -f                          do not sort, enable -aU, disable -ls --color
            -u                          with -lt: sort by, and show, access time;
                                        with -l: show access time and sort by name;
                                        otherwise: sort by access time, newest first
            -v                          natural sort of (version) numbers within text
            -S                          sort by file size, largest first
            --sort=WORD                 sort by WORD instead of name: none (-U), size (-S),
                                        time (-t), version (-v), extension (-X)
            -t                          sort by time, newest first; see --time
            --time=WORD                 change the default of using modification times;
                                        access time (-u): atime, access, use;
                                        change time (-c): ctime, status;
                                        birth time: birth, creation;
                                        with -l, WORD determines which time to show;
                                        with --sort=time, sort by WORD (newest first)
            --time-style=TIME_STYLE  	time/date format with -l; see TIME_STYLE below
            -U                          do not sort; list entries in directory order
            -X                          sort alphabetically by entry extension
            """
    for root, dirs, files in walk(path_name):
        for f in files:
            print(f)


ls = LS()
