#!/bin/usr/env python3.8

"""
Environment variables are often used for configuring command line tools and scripts. Write a script that does the following:
    Prints the first ten digits of PI to the screen.
    Accepts an optional environment variable called DIGITS. If present, the script will print that many digits of PI instead of 10.
"""

import math
import os

digits = (os.getenv("DIGITS"))

if digits:
    digits = int(digits)
else:
    digits=10

print("%.*f" % (digits,math.pi))







