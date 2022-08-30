#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat=[" ".join(["{:d}".format(i) for i in row]) for row in matrix]
    print("\n".join(mat))
