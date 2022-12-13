import unittest
import collections

def max_submatrix_area(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    max_area = 0

    heights = [0] * len(matrix[0])

    for row in matrix:
        min_height = float('inf')
        continous_ones_len_or_width = 0

        for index, cell in enumerate(row):

            # if current cell is zero then reset current min height 
            # and continuous ones length
            if not cell:
                min_height = float('inf')
                continous_ones_len_or_width = 0
                heights[index] = 0

                continue

            # Used to compute the wi
            continous_ones_len_or_width += 1

            # Increase height on each row
            heights[index] += 1

            min_height = min(min_height, heights[index])

            # Compute current area based on previous heights
            area = continous_ones_len_or_width * min_height
            max_area = max(max_area, area)

    return max_area

class Tests(unittest.TestCase):
    def test(self):
        mat = [
            [ 1, 1, 0, 1, 0],
            [ 1, 1, 1, 1, 1],
            [ 0, 1, 1, 1, 1],
            [ 0, 1, 1, 1, 1],
            [ 1, 1, 1, 0, 1],
        ]
        self.assertEqual(max_submatrix_area(mat), 12)

    def tests_all(self):
        rows = 24
        columns = 14
        submatrix_width = 7
        submatrix_height = 9

        mat = [[1 if i < submatrix_height and j < submatrix_width else 0 \
                for j in range(columns)] \
                    for i in range(rows)]

        # move the 3 x 3 square on each position within the greater matrix
        for r in range(rows - submatrix_height):
            # Allows shift the square back to first column
            for c in range(columns):
                # Test only if the square is within main matrix bounds
                if c + submatrix_width <= columns:
                    self.assertEqual(max_submatrix_area(mat), submatrix_height * submatrix_width)
                # shift right the ones square
                for row in range(r, r + submatrix_height):
                    mat[row] = mat[row][columns - 1:] + mat[row][:columns - 1]

            # now shift down the square
            mat = mat[rows - 1:] + mat[:rows - 1]

if __name__ == "__main__":
    unittest.main()