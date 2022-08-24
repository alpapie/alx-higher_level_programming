#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lt = number % -10
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lt))
else:
    gt = number % 10
    if gt > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, gt))
    elif gt == 0:
        print("Last digit of {} is {} and is 0".format(number, gt))
    elif gt < 6 and gt != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, gt))
