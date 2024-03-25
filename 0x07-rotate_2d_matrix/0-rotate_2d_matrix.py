#!/usr/bin/python3
"""
Implement an in-place algorithm to rotate an n x n 
2D matrix by 90 degrees clockwise
"""

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    The matrix must be edited in-place
    Matrix will have 2 dimensions and will not be empty
    """
    n = len(matrix)
    
    """transpose matrix"""
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    """reverse matrix"""
    for row in matrix:
        row.reverse()


    
