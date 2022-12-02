import unittest
from functools import lru_cache

# Count the number of ways to climb a staircase with n steps, 
# if you are allowed to climb either one step or two steps at a time
# Standing on step "0" is the initial value
@lru_cache(maxsize=None)
def count_ways_rec(steps: int) -> int:
    if steps <= 3:
        return steps

    one_step = count_ways_rec(steps - 1)
    two_steps = count_ways_rec(steps - 2)

    return one_step + two_steps

def count_ways_iterative(steps: int) -> int:
    if steps <= 1:
        return steps

    # on step 0
    back_two_step = 1
    back_one_step = 1

    for iteration_no in range(2, steps + 1):
        steps_count = back_one_step + back_two_step
        back_two_step = back_one_step
        back_one_step = steps_count

    return steps_count

class Tests(unittest.TestCase):
    def tests_rec(self):
        self.assertEqual(count_ways_rec(0), 0)
        self.assertEqual(count_ways_rec(1), 1)
        self.assertEqual(count_ways_rec(2), 2)
        self.assertEqual(count_ways_rec(3), 3)
        self.assertEqual(count_ways_rec(4), 5)

    def tests_iter(self):
        self.assertEqual(count_ways_iterative(0), 0)
        self.assertEqual(count_ways_iterative(1), 1)
        self.assertEqual(count_ways_iterative(2), 2)
        self.assertEqual(count_ways_iterative(3), 3)
        self.assertEqual(count_ways_iterative(4), 5)
        self.assertEqual(count_ways_iterative(33), count_ways_rec(33))

if __name__ == "__main__":
    unittest.main()
