
# Given an array of positive integers and a target sum, find two non-overlapping subarrays
# such that the sum of the elements of each array is equal to the given target sum, and their
# total length is minimal. Return their total length.

import unittest

def min_sums(numbers: list[int], target: int) -> int:
    print(*numbers, "->", target)

    min_len = float('inf')

    # Current sliding window sum
    window_sum = 0

    # The left most index of the sliding window
    # Used to contract the sliding window sum
    left = 0

    # Used to include in results only the non overalapping intervals
    # If a target sum is found then compute the min of the current
    # min length and the length of the previous found subarray.
    # Note: the +oo ensures that only lower previous values are picked.
    # For e.g. once the first subarray is found, its length value will
    # trail along until the next non-overlapping subarray is found.
    previous_len = [float('inf')] * len(numbers)

    # Expand to the right and contract from the left
    for right, number in enumerate(numbers):
        # (1) Trail previous value; see (2)
        previous_len[right] = previous_len[right - 1]

        # Expand window
        window_sum += number

        # Contract: if the sliding window becomes to large
        # substract elements from left side
        while window_sum > target:
            window_sum -= numbers[left]
            left += 1

        # Check if the current target sum after expand and contract was found
        if target == window_sum:
            length = right - left + 1

            # Actually updated after the second subarray is found
            # For the first subarray this value will be +oo
            min_len = min(min_len, length + previous_len[left - 1])

            # (2) save the length for later
            # In order to ensure we drag along only the min length subarray
            # update the current index only if current length is smaller than
            # previous; see (1)
            previous_len[right] = min(length, previous_len[right])

    print(*previous_len)

    if min_len == float('inf'):
        return 0

    return min_len

class TestSums(unittest.TestCase):
    def test(self):
        self.assertEqual(min_sums([1, 2, 1, 1, 1], 3), 5)
        self.assertEqual(min_sums([1, 2, 1, 1], 3), 0)
        self.assertEqual(min_sums([7, 1, 1, 1, 2, 1, 1], 2), 3)
        self.assertEqual(min_sums([2, 1, 7, 1, 2, 1, 1], 2), 2)

if __name__ == '__main__':
    unittest.main()