import unittest
import random
from functools import lru_cache
import sys

def can_interleave(first: str, second: str, target: str) -> bool:

    @lru_cache(maxsize=None)
    def helper(first_index, second_index) -> bool:
        target_index = first_index + second_index

        # Current state
        # a, suffix
        # b, suffix
        # t, suffix
        #
        # Note: suffix can be empty

        # Suceess: target can is obtained by interleaving the two strings
        if (target_index == len(target) and
            first_index == len(first) and
            second_index == len(second)):
            return True

        # Reach first string end
        if first_index == len(first):
            return second[second_index:] == target[target_index:]

        # Reach second string end
        if second_index == len(second):
            return first[first_index:] == target[target_index:]

        # Reach target string end
        if target_index == len(target):
            # Both input string didn't reach the end
            return False

        # At this point all strings didn't reach the last char

        target_char = target[target_index]

        if (first[first_index] == target_char and
            helper(first_index + 1, second_index)):
            return True

        if (second[second_index] == target_char and
            helper(first_index, second_index + 1)):
            return True

        return False

    if len(target) != len(first) + len(second):
        return False

    return helper(0, 0)

class Test(unittest.TestCase):
    def tests(self):
        self.assertTrue(can_interleave("abc", "def", "adbcef"))
        self.assertTrue(can_interleave("abc", "def", "deabfc"))
        self.assertFalse(can_interleave("abc", "bcd", "abcd"))
        self.assertFalse(can_interleave("abc", "bcd", "bacdef"))

    def test_all(self):
        def random_str(length):
            return ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(length)])

        target = random_str(1000)
        first = ''
        second = ''

        for ch in target:
            if random.randint(0, 1):
                second += ch
            else:
                first += ch

        self.assertTrue(can_interleave(first, second, target))

if __name__ == "__main__":
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(10000)
    print(sys.getrecursionlimit())
    unittest.main()
