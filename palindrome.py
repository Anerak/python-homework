#!/usr/bin/env python3
foo = input("Enter the possible palindrome: ")
# Remove the space
foo = foo.replace(" ", "").upper()
# We check if the reversed string is the same as the original. [::-1] reverses the string.
if foo[::-1] == foo: print("It's a palindrome")
else: print("Not a palindrome")
