#!/usr/bin/python3
# print the strig in uppercase with ord() and chr()

def uppercase(str):
    mot=""
    for char in str :
        if ord(char) >= 97 and ord(char) <= 122 :
            char = chr(ord(char) - 32)
            mot= mot + char
    print("{}".format(mot))
uppercase("holberton")