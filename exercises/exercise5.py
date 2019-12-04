#!/usr/bin/env python3.8

"""
Write a script that does the following:

Takes a port_number as its only argument.
Calls out to lsof to determine if there is a process listening on that port.
 1) If there is a process, kill the process and inform the user.
 2) If there is no process, print that there was no process running on that port.
 3) Improve your script to kill processes by exiting with an error status code when there isn.t a process to kill.
"""

import argparse
import subprocess
import os
import sys

parser = argparse.ArgumentParser(description='Kill process on  defined port')
parser.add_argument('port', type=int, help='A port to serach from [0-65535]')
args = parser.parse_args()

response = subprocess.run(['sudo', 'lsof','-i4TCP:%s' % args.port,'-Fp'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,)

pid= response.stdout.decode().strip()[1:]
#pid= response.stdout.decode().split()[10]  #for sudo lsof -i4TCP 
#print(pid)

if pid:
    os.kill(pid,9)
else:
    print(f'No process on port {args.port} running')
    sys.exit(1)

