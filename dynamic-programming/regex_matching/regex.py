import unittest
from functools import lru_cache

def regex_match(regex: str, input: str) -> bool:
    if not regex:
        return not input or len(input) == 0

    if not input:
        return False

    # Split into groups delimited by '*'
    groups = regex.split('*')

    @lru_cache(maxsize=None)
    def matcher(group_index: int, input_index: int) -> bool:
        if group_index == len(groups) and input_index == len(input):
            return True

        group = groups[group_index]
        index = input_index

        for ch in group:
            if ch != '.' and input[index] != ch:
                return False
            index += 1

        return matcher(group_index + 1, index)

    return matcher(0, 0)

class Tests(unittest.TestCase):
    def tests_empty(self):
        self.assertTrue(regex_match("", None))
        self.assertFalse(regex_match("a", None))
        self.assertTrue(regex_match("", None))
        self.assertTrue(regex_match("", ""))
        self.assertTrue(regex_match(None, None))

    def tests_simple(self):
        self.assertTrue(regex_match("aa", "aa"))
        self.assertTrue(regex_match("a.a", "aba"))
        self.assertTrue(regex_match("a.a.", "abax"))

if __name__ == "__main__":
    unittest.main()
