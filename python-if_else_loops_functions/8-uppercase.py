#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        letters = ord(letters)
        if 97 <= letters <= 122:
            letters -= 32
        print("{}".format(chr(letters)), end="")
