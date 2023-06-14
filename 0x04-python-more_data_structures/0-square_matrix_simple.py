#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return [[]]
    if len(matrix[0] == 0):
        return [[]]
    new_matrix = [[row[x ** 2] for row in matrix] for x in row]
    return new_matrix
