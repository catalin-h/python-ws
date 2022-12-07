import unittest
import math

# You are given a maze represented as a matrix. Cells that you cannot enter are marked with
# -1; the rest of the cells contain a non-negative integer that represents a score. The score of a
# path through the maze is equal to the sum of the scores of the cells traversed by that path.
def max_score(maze: list[list[int]]) -> int:
    if not maze or len(maze) == 0 or len(maze[0]) == 0 or \
        maze[0][0] == -1 or maze[-1][-1] == -1:
        return -1

    previous_row = [-1] * len(maze[0])
    previous_row[0] = 0

    # Since we can move from top to bottom
    # we can iterate from first to last row
    for row in maze:
        next_row = [-1] * len(row)

        # Since we can move from left to right
        # we iterate from first to last column in current row
        for index, cell in enumerate(row):

            # Skip Wall cell
            if cell == -1:
                continue

            # Check move from top to bottom
            # Note: previous cell might be a wall or -1
            if previous_row[index] != -1:
                next_row[index] = previous_row[index] + cell

            # Check move from left to right
            # Note: previous cell might be a wall or -1
            if index > 0 and next_row[index - 1] != -1:
                next_row[index] = max(next_row[index], next_row[index - 1] + cell)

        previous_row = next_row

    return previous_row[-1]

class Tests(unittest.TestCase):
    def test(self):
        maze = [[2]]
        self.assertEqual(max_score(maze), 2)
        maze = [
            [2, 3],
            [1, 1]
        ]
        self.assertEqual(max_score(maze), 6)
        maze = [
            [0, 1, 1],
            [9, 0, 3]
        ]
        self.assertEqual(max_score(maze), 12)

    def test_walls(self):
        maze = [
            [0, -1],
            [3, 0]
        ]
        self.assertEqual(max_score(maze), 3)
        maze = [
            [0, -1, 100],
            [0, 10, 0]
        ]
        self.assertEqual(max_score(maze), 10)

    def test_no_path(self):
        maze = [[-1]]
        self.assertEqual(max_score(maze), -1)
        maze = [
            [0, -1],
            [-1, 0]
        ]
        self.assertEqual(max_score(maze), -1)
        maze = [
            [0, -1, 0],
            [0, -1, 0]
        ]
        self.assertEqual(max_score(maze), -1)
    def test_perf(self):
        n = rows = 50
        m = columns = 30

        maze = [[ 1 ] * columns] * rows

        # Why n + m - 1 ?
        # - there are at least n - 1 steps down since
        # we don't count the first row
        # - for the first there can be max m steps
        # - since we move from left to right the total
        # number of steps are bound to n + m - 1 steps
        # from first and last cells
        self.assertEqual(max_score(maze), n + m - 1)

if __name__ == "__main__":
    unittest.main()
