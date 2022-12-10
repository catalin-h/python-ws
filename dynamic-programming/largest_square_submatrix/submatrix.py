import unittest

# You are given a matrix where elements are either 0 or 1. 
# Return the number of ones in the largest square-shaped 
# region of the matrix which contains only ones.
def max_square(matrix: list[list[int]]) -> int:

    # Compute the square size for the square at position (row, column)
    # The idea is to compute the min size of the squares A, B, C and add 1
    # in X. The square_sizes matrix contains the sizes for all possible squares.
    # Since has the same size as the input matrix, each cell represent the
    # bottom-right vertex of each square from the input matrix and the value
    # of the cell is the square edge length
    # . . . .
    # . . . . 
    # . A B .
    # . C X .
    # . . . .
    # 
    def square_size(square_sizes, row, column) -> int:
        cell = matrix[row][column]
        
        # Make sure we have at least 2 columns and rows and the
        # current element is not 0
        if row == 0 or column == 0 or not cell:
            return cell

        return 1 + min(square_sizes[row - 1][column - 1], \
                        square_sizes[row - 1][column], \
                        square_sizes[row][column - 1])

    rows = len(matrix)
    columns = len(matrix[0])

    square_sizes = [[0] * columns for _ in range(rows)]

    # In case of the Zero matrix the largest square is 0
    largest = 0

    for row in range(rows):
        for column in range(columns):
            size = square_size(square_sizes, row, column)
            square_sizes[row][column] = size
            largest = max(largest, size)

    return largest ** 2

class Tests(unittest.TestCase):
    def tests(self):
        mat = [
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
        ]
        self.assertEqual(max_square(mat), 9)

    def tests_all(self):
        rows = 24
        columns = 14
        square_size = 7

        mat = [[1 if i < square_size and j < square_size else 0 for j in range(columns)] for i in range(rows)]

        # move the 3 x 3 square on each position within the greater matrix
        for r in range(rows - square_size):
            # Allows shift the square back to first column
            for c in range(columns):
                # Test only if the square is within main matrix bounds
                if c + square_size <= columns:
                    self.assertEqual(max_square(mat), square_size ** 2)
                # shift right the ones square
                for row in range(r, r + square_size):
                    mat[row] = mat[row][columns - 1:] + mat[row][:columns - 1]

            # now shift down the square
            mat = mat[rows - 1:] + mat[:rows - 1]

if __name__ == "__main__":
    unittest.main()
