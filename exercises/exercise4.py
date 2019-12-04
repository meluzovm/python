#!/usr/bin/env python3.8
"""
Write a script that does the following:

    Receives a file_name and line_number as command line parameters.
    Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.

Make sure that you handle the following error cases by presenting the user with a useful message:

    The file doesn.t exist.
    The file doesn.t contain the line_number specified (file is too short).
"""

import argparse

parser = argparse.ArgumentParser(description="Outputs a specific line from file")
parser.add_argument('file_name', help='Name of file')
parser.add_argument('line_number', type=int, help='Line number')
args = parser.parse_args()

#file_name = input("Enter filename: ")
#line_number = int(input("Enter linenumber: "))

try:
    lines=open(args.file_name,'r').readlines()
    line=lines[args.line_number - 1].strip()
except OSError as err:
    print(f"ERROR: File {args.file_name} not found. Details: ",err)
except IndexError as err:
    print(f"ERROR: Line {args.line_number} not found. Details: ",err)
else:
    print(line)
