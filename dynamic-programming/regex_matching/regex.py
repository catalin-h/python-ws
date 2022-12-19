import unittest
from functools import lru_cache

def regex_match(regex: str, input: str) -> bool:
    if not regex:
        return not input or len(input) == 0

    if regex[0] == '*':
        return False

    # Find the indices of the multi char match (mcm)
    # groups = regex.split('*')
    groups = []
    start = 0
    for end, ch in enumerate(regex):
        if ch != '*':
            if end + 1 == len(regex):
                groups += [(start, end)]
            continue

        size = end - start + 1
        # Split the 'x*' group from the single char match gorup
        if size > 2:
            groups += [(start, end - 2)]

        groups += [(end-1, end)]
        start = end + 1

    @lru_cache(maxsize=None)
    def matcher(group_index: int, input_index: int) -> bool:
        def match_char(char_pattern, input_index):
            if input_index >= len(input):
                return False
            return char_pattern == '.' or char_pattern == input[input_index]

        if input is None:
            return False

        if group_index == len(groups):
            return input_index == len(input)

        start, end = groups[group_index]
        index = input_index

        # Match each char
        if regex[end] != '*':
            for ch in regex[start : end + 1]:
                if not match_char(ch, index):
                    return False
                index += 1

            return matcher(group_index + 1, index)

        while not matcher(group_index + 1, index) and index < len(input):
            if not match_char(regex[end - 1], index):
                return False
            index += 1

        return matcher(group_index + 1, index)

    return matcher(0, 0)

class Tests(unittest.TestCase):
    def test_perf(self):
        n = 100
        self.assertTrue(regex_match("a*", 'a' * n))
        self.assertTrue(regex_match("xa*y", 'x' + 'a' * n + 'y'))
        self.assertTrue(regex_match('x' + 'a*' * n + 'y', 'x' + 'a' * n + 'y'))

    def test_1(self):
        self.assertTrue(regex_match("a*", ''))
        self.assertTrue(regex_match("a*a", "aaa"))
        self.assertTrue(regex_match(".*a", "aaa"))
        self.assertTrue(regex_match(".*ad", "ad"))
        self.assertFalse(regex_match(".*ad", "ac"))
        self.assertTrue(regex_match("a*b*c*", ""))
        self.assertTrue(regex_match("a*b*c*", "a"))
        self.assertTrue(regex_match("a*b*c*", "ac"))
        self.assertTrue(regex_match("a*b*c*", "ab"))
        self.assertTrue(regex_match("a*b*c*", "b"))
        self.assertTrue(regex_match("a*b*c*", "bc"))
        self.assertTrue(regex_match("a*b*c*", "abc"))
        self.assertFalse(regex_match("a*b*c*", "xabcy"))
        self.assertTrue(regex_match("x.*y", "xabcy"))

    def test_empty(self):
        self.assertTrue(regex_match("", None))
        self.assertFalse(regex_match("a", None))
        self.assertTrue(regex_match("", None))
        self.assertTrue(regex_match("", ""))
        self.assertTrue(regex_match(None, None))

    def test_2_simple(self):
        self.assertTrue(regex_match("aa", "aa"))
        self.assertTrue(regex_match("a.a", "aba"))
        self.assertTrue(regex_match("a.a.", "abax"))
        self.assertTrue(regex_match("...", "abc"))
        self.assertFalse(regex_match("...", "ab"))
        self.assertFalse(regex_match("..", "abc"))

if __name__ == "__main__":
    unittest.main()
