import collections
import unittest
import functools

# Given an array of integers, find the contiguous subarray
# having the largest sum. Return its sum.
# Kadane's algorithm
def max_sum(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 0

    partial_sum = numbers[0]
    max_partial_sum = -float('inf')

    for n in numbers[1:]:
        partial_sum = max(n, partial_sum + n)
        max_partial_sum = max(max_partial_sum, partial_sum)

    return max_partial_sum

class TestCount(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_sum([-1, 1, 2, 3, -2]), 6)
        self.assertEqual(max_sum([-1, 1, 2, 3, -2, 3]), 7)
        self.assertEqual(max_sum([-1, 1, 2, -9, 4, -1]), 4)
        self.assertEqual(max_sum([-1, 4, -9, 1, 2, -1]), 4)
        self.assertEqual(max_sum([1] * 10), 10)
        self.assertEqual(max_sum([-1] * 10), -1)
        self.assertEqual(max_sum([]), 0)
        self.assertEqual(max_sum([1] * 1000000), 1000000)


if __name__ == '__main__':
    unittest.main()