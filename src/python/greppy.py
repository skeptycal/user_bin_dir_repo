#!/usr/bin/env python3

from pathlib import Path
from sys import argv

HERE = Path().cwd()

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

class styles:
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BRIGHT = '\033[5m'
    INVERTED = '\033[7m'
    RESET = '\033[0m'

# this is the #*--> search_flag_for_testing <--*#
# -------------------------------------
#  3 5 7 9 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3
#          1 3 5 7 9 1 3 5 7 9 1 3 5 7 9
# *it is at position 20 in line 31
# (lines start counting at 1, positions at 0)

def main(args=argv[1:]):
    line_no: int = 0
    char_no: int = 0
    for file_path in Path(HERE).rglob("*"):
        if not file_path.is_file():
            continue
        for arg in args:
            # print(f"searching {file_path.name} for {arg}")
            if arg in (data := file_path.open(mode='r').read()):
                for i, line in enumerate(data.split('\n')):
                    # print(i, ' - ', line)
                    if arg in line:
                        char_no = line.index(arg)
                        line_no = i
                        print(f"{colors.YELLOW}Found '{arg}' at {colors.RED}{styles.BRIGHT}line {line_no:<5} pos {char_no:<4}{styles.RESET}{colors.YELLOW} in '{file_path.name}'")
                # print('\n'.join([f"{i:>3} {line}" for i, line in data.split('\n')[line_no-2:line_no+3]]))
        # if any(args in Path(filename).open(mode='r')):
        #     print(f"found ")


if __name__ == "__main__":
    main()
