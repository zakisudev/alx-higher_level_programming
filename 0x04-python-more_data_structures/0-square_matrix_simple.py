#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [x**2 for elem in matrix for x in elem]
    return new_matrix
