#!/usr/bin/python3
import random
br = random.randint(-10000, 10000)

if br < 0:
    lt = br % -10
    print("Last digit of {} is {} and is less than 6 and not 0".format(nr, lt))
else:
    lt = br % 10
    if lt > 5:
        print("Last digit of {} is {} and is greater than 5".format(br, lt))
    elif lt == 0:
        print("Last digit of {} is {} and is 0".format(br, lt))
    elif lt < 6 and lt != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(br, lt))
