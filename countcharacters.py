#!/usr/bin/env python3
from os import strerror

dict = {}
inp = input("Name of the file: ")
try:
    with open(inp, 'r') as file:
        for i in file.read():
            for j in i:
                if (j == "\n") or (j.isspace()): continue
                else: j = j.lower()
                if j in dict: dict[j] += 1
                else: dict[j] = 1
except IOError as Error: print("Error: ", strerror(Error.errno))

for k in dict:
    print(f"{k} -> {dict[k]}")