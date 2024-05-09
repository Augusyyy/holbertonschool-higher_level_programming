#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix_sub = []
        for j in range(len(matrix[i])):
            new_matrix_sub.append(int(matrix[i][j]) ** 2)
        new_matrix.append(new_matrix_sub)
    return new_matrix
