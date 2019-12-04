#!/usr/bin/env python3.8

"""
Write a script that prompts the user for:

    A file_name where it should write the content.
    The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.

After the user enters an empty line, write all of the lines to the file and end the script.

"""

filename = input("Enter filename:")

with open(filename,'a') as f:
    while True:
        line=input().strip()
        if line == "":
            break
        else:
           f.write(line+"\n")
