import unittest
import math

# You are given a maze represented as a matrix, where cells you may enter are marked with
# zeroes, and walls are marked with ones. You start at the top-left corner, and need to reach
# the bottom-right corner. You are only allowed to move to the right or down, without passing
# through walls. Count how many distinct paths exist.
def paths(maze: list[list[int]]) -> int:
    if not maze or len(maze) == 0 or len(maze[0]) == 0 or \
        maze[0][0] == 1 or maze[-1][-1] == 1:
        return 0

    previous_row = [0] * len(maze[0])

    # Assume the first cell is not a wall
    previous_row[0] = 1

    # Since we can move from top to bottom
    # we can iterate from first to last row
    for row in maze:
        next_row = [0] * len(maze[0])

        # Since we can move from left to right
        # we iterate from first to last column in current row
        for index, cell in enumerate(row):

            # Skip Wall cell
            if cell == 1:
                previous_row[index] = 0
                continue

            next_row[index] = previous_row[index]

            if index > 0:
                next_row[index] += next_row[index - 1]

        previous_row = next_row

    return previous_row[-1]

class Tests(unittest.TestCase):
    def test(self):
        maze = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(paths(maze), 2)
        maze = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(paths(maze), 3)

    def test_walls(self):
        maze = [
            [0, 1],
            [0, 0]
        ]
        self.assertEqual(paths(maze), 1)
        maze = [
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(paths(maze), 1)

    def test_no_path(self):
        maze = [
            [0, 1],
            [1, 0]
        ]
        self.assertEqual(paths(maze), 0)
        maze = [
            [0, 1, 0],
            [0, 1, 0]
        ]
        self.assertEqual(paths(maze), 0)

    def test_perf(self):
        n = rows = 50
        m = columns = 20

        maze = [[ 0 ] * columns] * rows

        # Why C(n + m - 2, n - 1) ?
        # - there are at least n - 1 steps down
        # - since we move from left to right the total
        # number of steps are bound to n + m - 2 steps
        # from first and last cells
        self.assertEqual(paths(maze), math.comb(n + m - 2, n - 1))

if __name__ == "__main__":
    unittest.main()
