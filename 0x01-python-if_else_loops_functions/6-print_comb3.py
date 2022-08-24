#!/usr/bin/python3
for number1 in range(8):
    for number2 in range(10):
        if number1 < number2:
            print("{}{}".format(number1, number2), end=", ")
print("{}".format(89))
