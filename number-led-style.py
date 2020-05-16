#!/usr/bin/env python3

# Each index contains a the representation of a number (0-9)
digits = [
        "###\n# #\n# #\n# #\n###",
        "  #\n  #\n  #\n  #\n  #",
        "###\n  #\n###\n#  \n###",
        "###\n  #\n###\n  #\n###",
        "# #\n# #\n###\n  #\n  #",
        "###\n#  \n###\n  #\n###",
        "###\n#  \n###\n# #\n###",
        "###\n  #\n  #\n  #\n  #",
        "###\n# #\n###\n# #\n###",
        "###\n# #\n###\n  #\n###"
    ]

def nums(num):
    num = list(num)
    nxtPrnt = ""
    for i in range(5):
        for j in num:
            nxtPrnt += " " + digits[int(j)].split('\n')[i]
        print(nxtPrnt)
        nxtPrnt = ""

nums(input("Number: "))
