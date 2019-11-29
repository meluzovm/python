#!/usr/bin/env python3.8


filename = input("Enter filename:")

with open(filename,'a') as f:
    while True:
        line=input().strip()
        if line == "":
            break
        else:
           f.write(line+"\n")
 
        
        
