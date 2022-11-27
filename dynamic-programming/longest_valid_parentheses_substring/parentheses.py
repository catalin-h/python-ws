import unittest

# Build valid parentheses starting from small problems:
#
# Patterns:
# (1) use mirroring since a valid substring has an even length
# if } look for a match on left by computing the mirror:
# m           i-1, i
# { {.. inner ..} }
# ^-----outer-----^
# m = i - best[i-1] - 1
# if s[m] == { => found outer, best[i] = i - m + 1
#
# (2) Append or prepend disjoint groups
# 
# { .. new pair } { .. suffix ..}
# 
# best[i] += s[m-1]
# 
# s[m-1] is either 0 or some positive number
#
# (3) return max(best)
#
def longest_parentheses(s: str) -> int:
    best = [0] * (len(s) + 1)

    for i, ch in enumerate(s):
        # start new substring
        if i == 0 or ch == '{':
            continue
        
        # Check for closing parentheses
        # Note: only closing parentheses '}' contain best value
        if ch == '}':
            mirror = i - best[i-1] - 1

            # Found the outer substring
            if mirror >= 0 and s[mirror] == '{':
                best[i] = best[i-1] + 2

                # Try prepend previous substring next to current one
                if mirror > 0 and s[mirror - 1] == '}':
                    best[i] += best[mirror - 1]

    return max(best)

class ParensTest(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_parentheses('{}{{}}{'), 6)
        self.assertEqual(longest_parentheses(''), 0)
        self.assertEqual(longest_parentheses('}'), 0)
        self.assertEqual(longest_parentheses('{'), 0)
        self.assertEqual(longest_parentheses('}}}{{{'), 0)
        self.assertEqual(longest_parentheses('{}' + '}' + '{{}}' + '{'), 4)
        self.assertEqual(longest_parentheses('{{}}' + '}' + '{}' + '{'), 4)
        self.assertEqual(longest_parentheses('{{}}'), 4)
        self.assertEqual(longest_parentheses('{' + '{{}}'), 4)
        self.assertEqual(longest_parentheses('{{}}' + '}'), 4)
        self.assertEqual(longest_parentheses('{{}}' + '{'), 4)
        self.assertEqual(longest_parentheses('{}{}'), 4)
        self.assertEqual(longest_parentheses('{' + '{}{}'), 4)
        self.assertEqual(longest_parentheses('{}{}' + '{'), 4)
        self.assertEqual(longest_parentheses('{}{}' + '}'), 4)
        self.assertEqual(longest_parentheses('{}'), 2)
        self.assertEqual(longest_parentheses('{}' + '{'), 2)
        self.assertEqual(longest_parentheses('}' + '{}'), 2)
        self.assertEqual(longest_parentheses('{}' + '}'), 2)
        n = 1000
        k = 10
        s = ')'.join(['{' * n + '}' * n] * k)
        self.assertEqual(longest_parentheses(s), n * 2)
        s = ')'.join(['{}' * n] * k)
        self.assertEqual(longest_parentheses(s), n * 2)

if __name__ == "__main__":
    unittest.main()
