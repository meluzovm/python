#!/usr/bin/env python3.8


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

