# Question: Write a Python function to rotate a 2D matrix 90 degrees clockwise.
def rotate_matrix(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]
