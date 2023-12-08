#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Write a function that computes square of all integer of a matrix
    Arg:
    matrix (class of a list): The input matrix
    REturns:
    List of lists: the mayrix with square value
    """
    squared_matrix  = []
    for row in matrix:
        square_row = [num ** 2 for num in row]
        squared_matrix.append(square_row)

        return squared_matrix


if __name__ == "__main__":
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    new_matrix = square_matrix_simple(matrix)

    for row in ("Squared Matrix"):
        print(new_matrix)

    print(matrix)
