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

dict = {key: value for key, value in sorted(dict.items(),key=lambda item: item[1],reverse=True)}
try:
    with open(file.name.split(".")[0] + ".hist", "w") as newFile:
        for k in dict:
            newFile.write(f"{k} -> {dict[k]} \n")
except IOError as Error: print("Error: ", strerror(Error.errno))