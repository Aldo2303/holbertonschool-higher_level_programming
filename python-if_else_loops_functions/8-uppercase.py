#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) >= 97 and ord(letters) <= 122:
            letters = ord(letters) - 32
            print("{}".format(chr(letters)), end="")
        else:
            print("{}".format(chr(letters)))
