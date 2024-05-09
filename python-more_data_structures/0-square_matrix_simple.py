#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix_i = []
        for j in range(len(matrix[i])):
            new_matrix_i.append(int(matrix[i][j]) ** 2)
        new_matrix.append(new_matrix_i)

    return new_matrix
