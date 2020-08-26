#!/usr/bin/env python3
"""
GREPPY(1)                   AutoSys General Commands Manual                  GREPPY(1)

NAME
    greppy -- file searching utility

SYNOPSIS
    Usage: greppy [-abcdDEFGHhIiJLlmnOopqRSsUVvwxZ] [-A num] [-B num] [-C[num]] [-e pattern] [-f file] [--binary-files=value] [--color[=when]] [--colour[=when]] [--context[=num]] [--label] [--line-buffered] [--null] [pattern] [file ...]

OPTIONS
     -A num, --after-context=num
     -a, --text
     -B num, --before-context=num
     -b, --byte-offset
     -C[num, --context=num]
     -c, --count
     --colour=[when, --color=[when]]
     -D action, --devices=action
     -d action, --directories=action
     -E, --extended-regexp
     -e pattern, --regexp=pattern
     --exclude
     --exclude-dir
     -F, --fixed-strings
     -f file, --file=file
     -G, --basic-regexp
     -H
     -h, --no-filename
     --help
     -I
     -i, --ignore-case
     --include
     --include-dir
     -J, --bz2decompress
     -L, --files-without-match
     -l, --files-with-matches
     --mmap
     -m num, --max-count=num
     -n, --line-number
     --null  Prints a zero-byte after the file name.
     -O      (default = False)
     -o, --only-matching
     -p      (default = True)
     -q, --quiet, --silent
     -R, -r, --recursive
     -S      (default = False)
     -s, --no-messages
     -U, --binary
     -V, --version
     -v, --invert-match
     -w, --word-regexp
     -x, --line-regexp
     -y      Equivalent to -i.  Obsoleted.
     -Z, -z, --decompress
     --binary-files=value
     --context[=num] (default = 2)
     --line-buffered

     If no file arguments are specified, the standard input is used.

DESCRIPTION
     The grep utility searches any given input files, selecting lines that match one or more patterns.  By default, a pattern matches an input
     line if the regular expression (RE) in the pattern matches the input line without its trailing newline.  An empty expression matches
     every line.  Each input line that matches at least one of the patterns is written to the standard output.

     grep is used for simple patterns and basic regular expressions (BREs); egrep can handle extended regular expressions (EREs).  See
     re_format(7) for more information on regular expressions.  fgrep is quicker than both grep and egrep, but can only handle fixed patterns
     (i.e. it does not interpret regular expressions).  Patterns may consist of one or more lines, allowing any of the pattern lines to match
     a portion of the input.

     zgrep, zegrep, and zfgrep act like grep, egrep, and fgrep, respectively, but accept input files compressed with the compress(1) or
     gzip(1) compression utilities.


     -A num, --after-context=num
             Print num lines of trailing context after each match.  See also the -B and -C options.

     -a, --text
             Treat all files as ASCII text.  Normally grep will simply print ``Binary file ... matches'' if files contain binary characters.
             Use of this option forces grep to output lines matching the specified pattern.

     -B num, --before-context=num
             Print num lines of leading context before each match.  See also the -A and -C options.

     -b, --byte-offset
             The offset in bytes of a matched pattern is displayed in front of the respective matched line.

     -C[num, --context=num]
             Print num lines of leading and trailing context surrounding each match.  The default is 2 and is equivalent to -A 2 -B 2.  Note:
             no whitespace may be given between the option and its argument.

     -c, --count
             Only a count of selected lines is written to standard output.

     --colour=[when, --color=[when]]
             Mark up the matching text with the expression stored in GREP_COLOR environment variable.  The possible values of when can be
             `never', `always' or `auto'.

     -D action, --devices=action
             Specify the demanded action for devices, FIFOs and sockets.  The default action is `read', which means, that they are read as if
             they were normal files.  If the action is set to `skip', devices will be silently skipped.

     -d action, --directories=action
             Specify the demanded action for directories.  It is `read' by default, which means that the directories are read in the same man-
             ner as normal files.  Other possible values are `skip' to silently ignore the directories, and `recurse' to read them recursively, which has the same effect as the -R and -r option.

     -E, --extended-regexp
             Interpret pattern as an extended regular expression (i.e. force grep to behave as egrep).

     -e pattern, --regexp=pattern
             Specify a pattern used during the search of the input: an input line is selected if it matches any of the specified patterns.
             This option is most useful when multiple -e options are used to specify multiple patterns, or when a pattern begins with a dash
             (`-').

     --exclude
             If specified, it excludes files matching the given filename pattern from the search.  Note that --exclude patterns take priority
             over --include patterns, and if no --include pattern is specified, all files are searched that are not excluded.  Patterns are
             matched to the full path specified, not only to the filename component.

     --exclude-dir
             If -R is specified, it excludes directories matching the given filename pattern from the search.  Note that --exclude-dir pat-
             terns take priority over --include-dir patterns, and if no --include-dir pattern is specified, all directories are searched that
             are not excluded.

     -F, --fixed-strings
             Interpret pattern as a set of fixed strings (i.e. force grep to behave as fgrep).

     -f file, --file=file
             Read one or more newline separated patterns from file.  Empty pattern lines match every input line.  Newlines are not considered
             part of a pattern.  If file is empty, nothing is matched.

     -G, --basic-regexp
             Interpret pattern as a basic regular expression (i.e. force grep to behave as traditional grep).

     -H      Always print filename headers with output lines.

     -h, --no-filename
             Never print filename headers (i.e. filenames) with output lines.

     --help  Print a brief help message.

     -I      Ignore binary files.  This option is equivalent to --binary-file=without-match option.

     -i, --ignore-case
             Perform case insensitive matching.  By default, grep is case sensitive.

     --include
             If specified, only files matching the given filename pattern are searched.  Note that --exclude patterns take priority over
             --include patterns.  Patterns are matched to the full path specified, not only to the filename component.

     --include-dir
             If -R is specified, only directories matching the given filename pattern are searched.  Note that --exclude-dir patterns take
             priority over --include-dir patterns.

     -J, --bz2decompress
             Decompress the bzip2(1) compressed file before looking for the text.

     -L, --files-without-match
             Only the names of files not containing selected lines are written to standard output.  Pathnames are listed once per file
             searched.  If the standard input is searched, the string ``(standard input)'' is written.

     -l, --files-with-matches
             Only the names of files containing selected lines are written to standard output.  grep will only search a file until a match has
             been found, making searches potentially less expensive.  Pathnames are listed once per file searched.  If the standard input is
             searched, the string ``(standard input)'' is written.

     --mmap  Use mmap(2) instead of read(2) to read input, which can result in better performance under some circumstances but can cause undefined behaviour.

     -m num, --max-count=num
             Stop reading the file after num matches.

     -n, --line-number
             Each output line is preceded by its relative line number in the file, starting at line 1.  The line number counter is reset for
             each file processed.  This option is ignored if -c, -L, -l, or -q is specified.

     --null  Prints a zero-byte after the file name.

     -O      If -R is specified, follow symbolic links only if they were explicitly listed on the command line.  The default is not to follow
             symbolic links.

     -o, --only-matching
             Prints only the matching part of the lines.

     -p      If -R is specified, no symbolic links are followed.  This is the default.

     -q, --quiet, --silent
             Quiet mode: suppress normal output.  grep will only search a file until a match has been found, making searches potentially less
             expensive.

     -R, -r, --recursive
             Recursively search subdirectories listed.

     -S      If -R is specified, all symbolic links are followed.  The default is not to follow symbolic links.

     -s, --no-messages
             Silent mode.  Nonexistent and unreadable files are ignored (i.e. their error messages are suppressed).

     -U, --binary
             Search binary files, but do not attempt to print them.

     -V, --version
             Display version information and exit.

     -v, --invert-match
             Selected lines are those not matching any of the specified patterns.

     -w, --word-regexp
             The expression is searched for as a word (as if surrounded by `[[:<:]]' and `[[:>:]]'; see re_format(7)).

     -x, --line-regexp
             Only input lines selected against an entire fixed string or regular expression are considered to be matching lines.

     -y      Equivalent to -i.  Obsoleted.

     -Z, -z, --decompress
             Force grep to behave as zgrep.

     --binary-files=value
             Controls searching and printing of binary files.  Options are binary, the default: search binary files but do not print them;
             without-match: do not search binary files; and text: treat all files as text.

     --context[=num]
             Print num lines of leading and trailing context.  The default is 2.

     --line-buffered
             Force output to be line buffered.  By default, output is line buffered when standard output is a terminal and block buffered oth-
             erwise.

     If no file arguments are specified, the standard input is used.

ENVIRONMENT
     GREP_OPTIONS  May be used to specify default options that will be placed at the beginning of the argument list.  Backslash-escaping is not supported, unlike the behavior in GNU grep.

EXIT STATUS
     The grep utility exits with one of the following values:

     0     One or more lines were selected.
     1     No lines were selected.
     >1    An error occurred.

EXAMPLES
     To find all occurrences of the word `patricia' in a file:

           $ grep 'patricia' myfile

     To find all occurrences of the pattern `.Pp' at the beginning of a line:

           $ grep '^\.Pp' myfile

     The apostrophes ensure the entire expression is evaluated by grep instead of by the user's shell.  The caret `^' matches the null string
     at the beginning of a line, and the `\' escapes the `.', which would otherwise match any character.

"""

import enum

from pathlib import Path
from sys import argv, path as PYTHONPATH

from typing import Dict, List, Union

try:
    from asloguru import logger
except:
    print("logging not available")

PathLike = Union[Path, str, None]

HERE: PathLike = Path().cwd()


class colors(enum.Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


class styles:
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BRIGHT = "\033[5m"
    INVERTED = "\033[7m"
    RESET = "\033[0m"


# this is the #*--> search_flag_for_testing <--*#
# -------------------------------------
#  3 5 7 9 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3
#          1 3 5 7 9 1 3 5 7 9 1 3 5 7 9
# *it is at position 20 in line 31
# (lines start counting at 1, positions at 0)


def grep_files(
    files: Union[List[PathLike], PathLike] = HERE, pattern="*", args=argv[1:]
):
    """
        Usage: greppy [-abcdDEFGHhIiJLlmnOopqRSsUVvwxZ] [-A num] [-B num] [-C[num]] [-e pattern] [-f file] [--binary-files=value] [--color[=when]] [--colour[=when]] [--context[=num]] [--label] [--line-buffered] [--null] [pattern] [file ...]
    """
    line_no: int = 0
    char_no: int = 0
    for file_path in Path(HERE).rglob("*"):
        if not file_path.is_file():
            continue
        for arg in args:
            try:
                if arg in (data := file_path.open(mode="r").read()):
                    for i, line in enumerate(data.split("\n")):
                        if arg in line:
                            char_no = line.index(arg)
                            line_no = i
                            print(
                                f"{colors.YELLOW}Found {colors.BLUE}{arg}{colors.YELLOW} at {colors.RED}{styles.BRIGHT}line {line_no:<5} pos {char_no:<4}{styles.RESET}{colors.YELLOW} in {colors.MAGENTA}{file_path.name}{colors.YELLOW}"
                            )
            except:
                pass


@logger.catch()
def main(args=argv[1:]):
    print(grep_files())


if __name__ == "__main__":
    main()
