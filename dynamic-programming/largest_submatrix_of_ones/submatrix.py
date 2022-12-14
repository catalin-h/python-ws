import unittest
import sys, os
import largest_rectangle_in_skyline.rectangle as sk

def max_submatrix_area_wrong(matrix: list[list[int]]) -> int:
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

def max_submatrix_area(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    max_area = 0
    heights = [0] * len(matrix[0])

    for row in matrix:
        for index, cell in enumerate(row):
            # if current cell is zero then reset current height
            if not cell:
                heights[index] = 0
                continue

            # Increase height on each row
            heights[index] += 1

        # Compute the max rectagle area at this row using
        # the max rectangle in skyline
        area = sk.max_rectangle_fast(heights)
        #area = sk.find_largest_rectangle(heights)
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

        mat = [
            [ 1, 1, 0, 1, 0],
            [ 1, 1, 1, 1, 1],
            [ 0, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1],
            [ 1, 1, 1, 0, 1],
        ]
        self.assertEqual(max_submatrix_area(mat), 12)

    def tests_all(self):
        rows = 8
        columns = 9
        submatrix_width = 3
        submatrix_height = 4

        mat = [[1 if i < submatrix_height and j < submatrix_width else 0 \
                for j in range(columns)] \
                    for i in range(rows)]

        # move the 3 x 3 square on each position within the greater matrix
        for r in range(rows - submatrix_height):
            # Allows shift the square back to first column
            for c in range(columns):
                # Test only if the square is within main matrix bounds
                if c + submatrix_width <= columns:
                    self.assertEqual(max_submatrix_area(mat), submatrix_height * submatrix_width, mat)

                # shift right the ones square
                for row in range(r, r + submatrix_height):
                    mat[row] = mat[row][columns - 1:] + mat[row][:columns - 1]

                # Note: the wrong version fails to find the largest rectangle
                # because it takes into account the minimum at each row instead
                # of applying the algorithm from largest rectangle from skyline.
                mat[r + submatrix_height - 1][c] = 1

            # now shift down the square
            mat = mat[rows - 1:] + mat[:rows - 1]

if __name__ == "__main__":
    unittest.main()