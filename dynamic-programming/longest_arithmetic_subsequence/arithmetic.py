import unittest
import collections

# Given a vector of integers numbers, return the length of the longest arithmetic subsequence.
# Must consider both increasing and decreasing subsequences.
# E.g.  1, 2, 3, 5, 8, 7 -> 1, 3, 5, 7
#       8, 7, 6, 4, 1, 2 -> 8, 6, 4, 2
#       2, 2, 2 -> 2, 2, 2
# 
# Note: in a arithmetic subsequence the next number is computed by adding a constant
def longest_arithmentic_sequence(numbers: list[int]) -> int:
    if not numbers:
        return 0
    elif len(numbers) == 1:
        return 1

    best = 0

    # At each index maintain a mapping between arithmetic step and sequence count.
    # The idea is to traverse the list and then reiterate this list and increase the
    # sequence count for each step at some previous index.
    # Note:
    # - that the step can be negative.
    # - smaller subsequences for the same step at some index are eliminated when
    # max is computed
    # - if there are more that 2 numbers in the list the minimum increasing subsequence is 2
    best_subseq_at = [{} for _ in range(len(numbers))]

    for i, number in enumerate(numbers):
        # iterate previously computes subsequences and try to add the current number
        for j in range(i):
            # compute the step in order to know to which bin we put the current number
            step = number - numbers[j]

            # For each previous number we have the option to:
            # - create a new subsequence of length 2
            # - add the previous subsequence with the current step at 
            # index "j" to index "i" and increase the length
            previous_best = best_subseq_at[j].get(step, 0)
            current_best = max(2, previous_best + 1)

            # in order to find the current best must update at current index
            # the subsequence length 
            best_subseq_at[i][step] = current_best

            # compute the current longest subsequence on the go
            best = max(best, current_best)

    return best

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_arithmentic_sequence([1, 2, 3, 5, 8, 7]), 4)
        self.assertEqual(longest_arithmentic_sequence([1, 2, 3, 5, 8, 7][::-1]), 4)
        self.assertEqual(longest_arithmentic_sequence([]), 0)
        self.assertEqual(longest_arithmentic_sequence([1]), 1)
        self.assertEqual(longest_arithmentic_sequence([1, 3]), 2)
        self.assertEqual(longest_arithmentic_sequence(list(range(5))), 5)

if __name__ == "__main__":
    unittest.main()
