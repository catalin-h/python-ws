from collections import Counter
import unittest
import math

def load_from_file():
    target = None
    numbers = None
    with open('input.txt', 'r') as f:
        target = int(f.readline())
        numbers = [int(x) for x in f.readline().split(' ') if x.isdecimal()]

    print(target, numbers)
    return (target, numbers)

def target_sum(target_sum:  int, numbers: list[int]) -> int:
    """ Computes the number of expressions to a target sum
        Time complexity O(S*n), S = sum(numbers), n = len(numbers)
    """
    if target_sum < 0 or len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        if target_sum == numbers[0]:
            return 1
        return 0

    # Note: the first number is always added, the next ones are
    # added or substracted
    partial_sums = Counter({numbers[0]: 1})

    # Note: iterate over numbers in order to avoid multiple
    # add or sub from the same number; in order words we
    # need to add and substract each number exactly once.
    for number in numbers[1:]:
        next_partial_sums = Counter()

        # iterate over the current partial sums in order to
        # compute the next partial sums by adding and substracting
        # the current number
        for partial_sum, count in partial_sums.items():
            sum_minus = partial_sum - number
            sum_plus = partial_sum + number

            # Note: there is no need to add +1 to the count as
            # the number of ways to reach to the new sum is the
            # same as reaching to current partial_sum
            next_partial_sums[sum_minus] += count
            next_partial_sums[sum_plus] += count

        partial_sums = next_partial_sums

    return partial_sums.get(target_sum, 0)

class TestTargetSums(unittest.TestCase):
    def test_extreme(self):
        # 1 +/- 1 ... +/- 1
        # n = 20
        # total count of numbers with signs = n - 1, for the first number is always +
        # if 1/2 of numbers are + and 1/2 are - then the sum is 0
        # so the total expressions where 1/2 have - sign = Comb(n - 1, n/2), meaning
        # n - 1 choose n/2 or from the n-1 total signs in how many ways we can have n/2
        # of half of the number with "-" sign.
        n = 20
        num = target_sum(0, [1] * n)
        comb = math.comb(n - 1, n//2)
        self.assertEqual(num, comb)

        n = 13
        # Note: for odd numbers we have 1 (first one) + n/2 numbers "+" and n/2 with "-"
        # so the sum will be 1
        num = target_sum(1, [1] * n)
        comb = math.comb(n - 1, n//2)
        self.assertEqual(num, comb)

    def test_input_txt(self):
        sum, numbers = load_from_file()
        self.assertEqual(target_sum(sum, numbers), 3)
    
    def test_normal(self):
        self.assertEqual(target_sum(2, [2, 1, 1]), 2)
        self.assertEqual(target_sum(1, [1, 4, 3, 1]), 2)

    def test_edge(self):
        self.assertEqual(target_sum(2, []), 0)
        self.assertEqual(target_sum(2, [2]), 1)
        self.assertEqual(target_sum(3, [2]), 0)

if __name__ == '__main__':
    unittest.main()