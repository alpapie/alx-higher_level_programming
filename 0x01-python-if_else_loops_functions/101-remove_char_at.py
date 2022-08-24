#!/usr/bin/python3
def remove_char_at(str, n):
    char_to_be_removed = 0
    blank = ""
    for character in str[:]:
        if char_to_be_removed != n:
            blank = blank + character
        char_to_be_removed += 1
    return blank
