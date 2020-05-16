#!/usr/bin/env python3
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

def nums(numero):
    numero = list(numero)
    nxtPrnt = ""
    for i in range(5):
        for j in numero:
            nxtPrnt += " " + digits[int(j)].split('\n')[i]
        print(nxtPrnt)
        nxtPrnt = ""

nums(input("Number: "))