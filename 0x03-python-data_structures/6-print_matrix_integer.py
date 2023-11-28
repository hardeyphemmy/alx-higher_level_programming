#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Function that print matrix of integers
    """
    for row in matrix:
        row_ele = ''.join("{} ".format(element, end=" ") for element in row)
        print(row_ele)


if __name__ == "__main__":
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    print_matrix_integer(matrix)
