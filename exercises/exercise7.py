#!/usr/bin/env python3.8
"""
Read file 
    1. Find number of char
    2. Find number of words
    3. Replace "." to "!"
    4. Save result to another file
"""

from  argparse import ArgumentParser

parser = ArgumentParser(description='Read file and do different manipulations with it')
parser.add_argument('file',help='location of file')
parser.add_argument('output',help='location of output file')

args = parser.parse_args()
print(args)

#try:
with open(args.file,'r') as f:
#except:
#    print('ERROR')
#else:
    content = f.read()
    print(f'Length of file is: { len(content) }')
    print(f'Number of words: { len(content.strip().split()) }')
    print(f'Replace \'.\' to \'!\' and  save result to {args.output}')
    with open(args.output,'w') as f2:
        f2.write(content.replace('.','!'))



