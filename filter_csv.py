# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa
#
# The argument parser is finished for you. Complete the TODO.

import argparse
import csv

def main():
    parser = argparse.ArgumentParser(description="Filter CSV rows by column value")
    parser.add_argument("filename", help="The CSV file to filter")
    parser.add_argument("column", help="The column name to filter by")
    parser.add_argument("value", help="The value to match")

    args = parser.parse_args()

    with open(args.filename, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        
        if args.column in header:
            col_index = header.index(args.column)
            for row in reader:
                if len(row) > col_index and row[col_index] == args.value:
                    print(",".join(row))

if __name__ == "__main__":
    main()