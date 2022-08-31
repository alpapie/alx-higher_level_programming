#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    weighted_avg = 0
    size = 0
    for tup in my_list:
        weighted_avg += (tup[0] * tup[1])
        size += tup[1]
    return weighted_avg / size
