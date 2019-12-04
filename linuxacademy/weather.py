#!/usr/bin/env python3.8
#####!/home/user/venvs/experiment/bin/python
# We.re going to write up the start of a script that can provide us with weather information using data from openweathermap.org.

# openweather api-key: 7dd65ea2d39ab5278db7f6d538d14fd
# example: api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=c7dd65ea2d39ab5278db7f6d538d14fd


import os
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='get current info for your zip code')
parser.add_argument('zip',help='zip code')
parser.add_argument('--country','-c',help='country code (2 digits)',default='de' )
args= parser.parse_args()


api_key = os.getenv('OWM_API_KEY')

if not api_key:
    print("Error: no API key")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"
#header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print(url)
res = requests.get(url)
#res = requests.get(url,headers=header)

if res.status_code != 200:
    print(f"Error. Responce code: {res.status_code}")
    sys.exit(1)

print(res.json())
