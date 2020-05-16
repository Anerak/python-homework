#!/usr/bin/env python3
def isanagram(base, compare):
    base, compare = base.replace(" ", "").upper(), compare.replace(" ", "").upper()
    print(base, compare)
    if (base == "") or (compare == ""): return "Not anagrams"
    
    for j in compare:
        if j in base:
            if compare.count(j) == base.count(j): continue
            else: return "Not anagrams"
        else: return "Not anagrams"
    return "Anagrams"

print(isanagram(input("First text:"), input("Compare with:")))