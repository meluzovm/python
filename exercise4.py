#!/usr/bin/env python3.8

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



