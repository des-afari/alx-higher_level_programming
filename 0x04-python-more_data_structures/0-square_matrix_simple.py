#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        return [[int(cell)**2 for cell in row] for row in matrix]
