#!/usr/bin/env python3
def getLifeDigit(num, final = False):
    r = 0
    for i in num:
        r += int(i)
    if final: return r
    else: return getLifeDigit(str(r), True)

print(getLifeDigit(input("Date of Birth: ")))