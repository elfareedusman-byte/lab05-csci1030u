# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern."
    )
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignore case sensitivity")

    args = parser.parse_args()

    search_pattern = args.pattern.lower() if args.ignore_case else args.pattern

    with open(args.filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            clean_line = line.rstrip("\n")
            check_line = clean_line.lower() if args.ignore_case else clean_line
            
            if search_pattern in check_line:
                print(f"{line_num}: {clean_line}")

if __name__ == "__main__":
    main()