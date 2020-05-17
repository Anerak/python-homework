#!/usr/bin/env python3
def findWord(word, mix):
    lastfound = 0
    for i in word:
        foundit = mix.find(i, lastfound)
        # .find may return -1 if it doesn't find the letter.
        if foundit != -1:
            lastfound = mix.index(i, lastfound)
        else: return "No"
    return "Yes"

print(findWord(input("Word to find: "), input("Mix of letters: ")))