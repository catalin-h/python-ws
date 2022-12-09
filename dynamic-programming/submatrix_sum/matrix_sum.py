import unittest
import random

# You are given a matrix of integers, and a list of queries of the form (top, left, bottom,
# right). For each query, you must compute the sum of the elements of the rectangle formed
# by matrix cells with row indices in [top, bottom) and [left, right). Return the result
# as a list.
def submatrix_sum_slow(matrix: list[list[int]], queries: list) -> list[int]:
    def sub_matrix_sum(top, bottom, left, right):
        s = 0
        for i in range(top, bottom):
            for j in range(left, right):
                s += matrix[i][j]
        return s

    return [sub_matrix_sum(top, bottom, left, right) for top, bottom, left, right in queries]

def submatrix_sum_fast(matrix: list[list[int]], queries: list) -> list[int]:
    # Use the matrix prefix sums to compute a inner matrix 
    # For e.g. to compute <ABCD> = <OA> + <OC> - <OD> - <OB>
    #
    #   O##|####|###
    #   ###|####|###
    #   ---C----D###
    #   ###|####|###
    #   ---B----A###
    #   ############
    # 
    # Points A = <bottom, right>, B = <bottom, left>, C = <top, left>, D = <top, right>
    def sub_matrix_sum(prefix_sums, top, bottom, left, right):
        return prefix_sums[bottom][right] + prefix_sums[top][left] - \
                (prefix_sums[top][right] + prefix_sums[bottom][left])

    # Add one row and one column in order to compute zero based coordinates
    rows = len(matrix) + 1
    columns = len(matrix[0]) + 1

    # Note: duplicates the same row
    # prefix_sums = [[0] * columns] * rows
    prefix_sums = [[0] * columns for _ in range(rows)] 

    # Compute first prefix sums for each row
    for row in range(1, rows):
        for column in range(1, columns):
            prefix_sums[row][column] = prefix_sums[row][column - 1] + matrix[row - 1][column - 1]

    # Compute prefix sums for each column
    for column in range(1, columns):
        for row in range(1, rows):
            prefix_sums[row][column] += prefix_sums[row - 1][column]

    return [sub_matrix_sum(prefix_sums, top, bottom, left, right) \
            for top, bottom, left, right in queries]

class Tests(unittest.TestCase):
    def test(self):
        n = 5
        mat = [[1] * n] * n 
        self.assertEqual(submatrix_sum_slow(mat, [[0, 2, 0, 2], [0, n, 0, n]]), [4, n * n])

    def test_all_one(self):
        n = 5
        mat = [[1] * n] * n 
        self.assertEqual(submatrix_sum_fast(mat, [[0, 2, 0, 2], [0, n, 0, n]]), [4, n * n])

    def test_all(self):
        n = 10
        mat = [[random.randrange(100) for _ in range(n)] for _ in range(n)]
        q = []

        # Compute all possible rectangles
        # Note: i <= ii and j <= jj
        for i in range(n):
            for ii in range(i, n):
                for j in range(n):
                    for jj in range(j, n):
                        q.append([i, ii, j, jj])
        a = submatrix_sum_slow(mat, q)
        b = submatrix_sum_fast(mat, q)
        self.assertEquals(a, b)

if __name__ == "__main__":
    unittest.main()