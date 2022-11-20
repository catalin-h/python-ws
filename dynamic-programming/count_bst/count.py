import collections
import unittest
import functools

# Given a list of distinct numbers, count how many distinct binary search trees can be formed
# to store the numbers.

# Note:
# - conclude that the total number of ways doesn't depend on the actual numbers but
# on their count.
# - empty or zero itemss is also unique
def count_bsts(items: list[int]) -> int:

    @functools.lru_cache(maxsize=None)
    def helper(count: int) -> int:
        if count <= 1:
            return 1
        
        ans = 0

        # Fix the root at each item index
        # Note: start from index 0 in order to place all items in one child
        for i in range(count):
            ans_left = helper(i)

            # extract one item for the root
            ans_right = helper(count - i - 1)

            # For the root as i-th element the total number
            # of possibilities is the product
            ans += ans_left * ans_right

        return ans

    return helper(len(items))

class TestCount(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(count_bsts([]), 1)
        self.assertEqual(count_bsts([1,2]), 2)
        self.assertEqual(count_bsts([1,4,5]), 5)

if __name__ == '__main__':
    unittest.main()