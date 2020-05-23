#!/usr/bin/env python3
from os import strerror

class DataException (Exception):
    pass
class WrongLine(DataException):
    def __init__(self, msg = "Wrong line"):
        DataException.__init__(self, msg)
class EmptyFile(DataException):
    def __init__(self, msg = "Empty file but exists"):
        DataException.__init__(self, msg)

try:
    with open(input("File name: "), 'r') as file:
        notes = {}
        for i in file.readlines():
            data = i.replace("\n", "").split("\t")
            name = f"{data[0]} {data[1]}"
            if name in notes: notes[name] += float(data[2])
            else: notes[name] = float(data[2])
        notes = {key: value for key, value in sorted(notes.items())}
        
        for a in notes:
            print(f"{a}\t{notes[a]}")
except Exception as excp:
    exit(print(excp))