import unittest
import collections
import random

# You are given a skyline where all buildings are rectangular and have the same width. The
# skyline is encoded as an array of heights.
# Return the area of the largest rectangle in the skyline that is covered by buildings.
# Example: skyline = [1, 3, 5, 4, 2, 5, 1]. The largest rectangle has area 10:
def max_rectangle_slow(skyline: list[int]) -> int:
    max_area = 0

    for index, height in enumerate(skyline):

        # compute the area if the rectangle containing
        # equal or lower buildings than current
        min_height = height

        for next, next_height in enumerate(skyline[index:]):
            min_height = min(min_height, next_height)
            max_area = max(max_area, (next + 1) * min_height)
    
    return max_area

def max_rectangle_fast(skyline: list[int]) -> int:
    # define named tuple
    Building = collections.namedtuple('Building', ['index', 'height'])

    max_area = 0

    # Contains a monotonic increasing sequence of heights and indices.
    # When iterating from left to right we build this increasing sequence.
    # If the next is higher than top item we push it to the stack but if
    # it's lower or equal then we start to unwind until we establish the
    # invariant again.
    # When poping the items we compute max area against the index of the
    # first top element.
    left_stack = collections.deque([])

    # Unwinding:
    #      
    #        #  -> 6 x 1
    #      # #  -> 5 x 2
    #      # # 
    #    # # #  -> 3 x 3
    #    # # # #
    #  # # # # # -> stop
    #  1 3 5 6 2
    #          ^
    #         start unwind
    for index, building_height in enumerate(skyline):

        # if higher add the  building to stack
        if not left_stack or left_stack[-1].height < building_height:
            left_stack.append(Building(index, building_height))
            continue

        # If lower unwind the stack and pop all buildings that are higher
        # than current building and compute the max rectangle
        last_index = index
        while left_stack and left_stack[-1].height >= building_height:
            last_index = left_stack[-1].index
            width = index - left_stack[-1].index
            max_area = max(max_area, width * left_stack[-1].height)
            left_stack.pop()

        # Now the stack contains no buildings or the last one in stack is smaller than
        # current building.
        # Add a pseudo-building in place of the removed ones plus the current building
        left_stack.append(Building(last_index, building_height))

    while left_stack:
        width = len(skyline) - left_stack[-1].index
        max_area = max(max_area, width * left_stack[-1].height)
        left_stack.pop()

    return max_area

def find_largest_rectangle(skyline):
    # Pad the skyline with zero, to avoid having to clean up
    # left_candidates at the end of the iteration.
    skyline = skyline + [0]
    num_buildings = len(skyline)
    Candidate = collections.namedtuple('Candidate', ['index', 'height'])
    left_candidates = []
    largest_area = 0

    for right in range(num_buildings):
        height = skyline[right]
        # Left pointer of the next candidate to be created.
        next_left = right

        while left_candidates and left_candidates[-1].height >= height:
            # Update area.
            # We remove the rectangle starting at left and ending
            # at right­1. It has height left_candidates[­1].height.
            left = left_candidates[-1].index
            width = right - left
            area = width * left_candidates[-1].height
            largest_area = max(largest_area, area)
            # Possible next candidate by trimming down the building.
            next_left = left
            del left_candidates[-1]

        left_candidates.append(Candidate(index=next_left, height=height))

    return largest_area

class Tests(unittest.TestCase):
    def tests(self):
        skyline = [1, 3, 5, 4, 2, 5, 1]
        self.assertEqual(max_rectangle_slow(skyline), 10)
        self.assertEqual(max_rectangle_fast(skyline), 10)
        skyline = [1, 3, 5, 4, 2, 5, 1, 3]
        self.assertEqual(max_rectangle_slow(skyline), 10)
        self.assertEqual(max_rectangle_fast(skyline), 10)
        skyline = [1, 3, 5, 4, 2, 5, 0, 3]
        self.assertEqual(max_rectangle_slow(skyline), 10)
        self.assertEqual(max_rectangle_fast(skyline), 10)
        skyline = [1, 2, 3, 4, 5]
        self.assertEqual(max_rectangle_slow(skyline), 9)
        self.assertEqual(find_largest_rectangle(skyline), 9)
        self.assertEqual(max_rectangle_fast(skyline), 9)

    def test_all(self):
        n = 100
        skyline = [random.randint(0, 20) for _ in range(n)]
        print(skyline)
        self.assertEqual(max_rectangle_slow(skyline), max_rectangle_fast(skyline))

if __name__ == "__main__":
    unittest.main()
