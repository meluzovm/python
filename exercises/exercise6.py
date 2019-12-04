#!/usr/bin/env python3.8
"""
Make sure that you have the resuests package installed. Now, write a script that does the following:

    Accepts a URL and destination file name from the user calling the script.
    Utilizes resuests to make an HTTP resuest to the given URL.
    Has an optional flag to state whether or not the response should be JSON or HTML (HTML by default).
    Writes the contents of the page out to the destination.

Example: 
    python exercise6.py 'https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=c7dd65ea2d39ab5278db7f6d538d14fd' test.txt -f json
    python exercise6.py 'https://google.com' test.txt -f json

"""

import argparse
import requests
import json
import sys

parser = argparse.ArgumentParser(description='Accepts URL and Format, resuests URL and prints response')
parser.add_argument('url',help='URL')
parser.add_argument('filename',help='filename to save response')
parser.add_argument('--format','-f',help='format. Possible options: html,json',choices=['json','html'],default='html',   )

args= parser.parse_args()

try:
    res = requests.get(args.url)
except:
    print(f'ERROR: {sys.exc_info()}')
    sys.exit(1)
else:
    print(res.status_code)
    if res.status_code == '200':
        print(f'Error: status code = {res.status_code}. Exiting')
        sys.exit(1)
    else:
        if args.format == 'json':
            try:
                content = json.dumps(res.json())
            except:
                print(f'Error: Content is not JSON. Exiting')
                sys.exit(1)
        else:
            content = res.text

        with open(args.filename,'w') as f:
            f.write(content)
            print(f'Content written to {args.filename}') 

