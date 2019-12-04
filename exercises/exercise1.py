#!/usr/bin/env python3.8
"""
Write a script that does the following:

    Prompts the user for a message to echo.
    Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
    Defines a function that takes a message and count then prints the message that many times.

To end the script, call the function with the user-defined values to print to the screen.
"""

message = input("Enter a message to echo:")
count = input("Enter number of times to repeat: ")

if count:
    count=int(count)
else:
    count=1

def print_message(mes,count):
    for i in range(count):
        print(mes)

print_message(message,count)

