#!/usr/bin/env python3
def change(letter, val):
    isup = letter.isupper() if True else False
    letter = letter.upper()

    if (ord(letter) + val) > 90:
        diff = (ord(letter) + val) - 90
        letter = chr(64 + diff)
        print(letter)
        if isup: return letter
        else: return letter.lower()
    else:
        letter = chr(ord(letter) + val)
        if isup: return letter
        else: return letter.lower()


def caesar(word, val):
    val = int(val)
    if (val < 1) and (val > 25):
        return "Invalid range of value."
    result = ""
    for i in word:
        if i.isalpha: result += change(i, val)
        else: result += i
    return result

print(caesar(input("Message: "),input("Number: ")))