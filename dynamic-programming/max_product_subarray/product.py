import collections
import unittest
import functools

# Note:
# Compact and clever code vs. longer but simpler
# Making the code compact and clever may come at the expense of readability. 
# Competitive programming resources are often biased towards short and clever implementations.
# In a software engineering position, these are usually frowned upon, since the code may
# become hard to understand and maintain. Avoid writing the code too cryptic/clever
# during the interview, since it may be seen as a negative point.

def find_non_zero_chunks(numbers: list[int]):
    chunk = []

    for n in numbers + [0]:
        if n == 0:
            yield chunk
            chunk = []
        else:
            chunk.append(n)

def find_max_product(numbers: list[int]) -> int:
    max_prod = 0
    product = 1

    for n in numbers:
        product *= n
        max_prod = max(max_prod, product)
    
    return max_prod

def max_product(numbers: list[int]) -> int:
    max_prod = 0
    for chunk in find_non_zero_chunks(numbers):
        # Note:
        # - the max_product is the current max product regardless
        # if it was computed with negatives or not
        # - to handle the case of odd negatives must also compute the product in reverse
        # order so we don't include the first negative number in the max product; the same
        # as when we iterate in original order we exclude the last negative number because
        # the product becomes negative ;)
        # - chunk[::-1] is the reversed list
        max_prod = max(max_prod, find_max_product(chunk), find_max_product(chunk[::-1]))

    return max_prod

def find_max_product(numbers: list[int]) -> int:
    # the current max element product
    max_product = 0

    # keep current max positive product in order to compute the min negative product
    # if the next element is negative; the latter is used to compute the current
    # max positive product
    max_positive_product = -float('inf')
    min_negative_product = float('inf')

    for number in numbers:

        # Compute the next max positive product
        if number > 0 and max_positive_product > 0:
            next_max_positive_product = number * max_positive_product
        else:
            # ignore the next max
            # number is <= 0 or max_positive_product <= 0
            next_max_positive_product = -float('inf')

        # get max flip from negative
        if number < 0 and min_negative_product < 0:
            next_max_positive_product_flip = number * min_negative_product
        else:
            # ignore
            next_max_positive_product_flip = -float('inf')

        # Compute the next min positive product
        if number > 0 and min_negative_product < 0:
            next_min_negative_product = number * min_negative_product
        else:
            # ignore the next min
            next_min_negative_product = float('inf')

        # get next min from flipping the max product
        if number < 0 and max_positive_product > 0:
            next_min_negative_product_flip = number * max_positive_product
        else:
            # ignore this value
            next_min_negative_product_flip = float('inf')

        # compute the next min negative and max positive products
        max_positive_product = max(number, next_max_positive_product, next_max_positive_product_flip)
        min_negative_product = min(number, next_min_negative_product, next_min_negative_product_flip)

        # compute the current max product
        max_product = max(max_product, max_positive_product)

    return max_product

class Tests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_product([1 , -2, 3, -4, -5, 6]), 360)
        self.assertEqual(find_max_product([1 , -2, 3, -4, -5, 6]), 360)
        self.assertEqual(find_max_product([1,  2,  3]), 6)
        self.assertEqual(find_max_product([1, -2, -3]), 6)
        self.assertEqual(find_max_product([1, -2, -3, -4, -5]), 120)
        self.assertEqual(find_max_product([1,  2, -3]), 2)
        self.assertEqual(find_max_product([1, -2, -3, -4, 5]), 60)
        self.assertEqual(find_max_product([1,  2,  3,  0, 4, 1]), 6)
        self.assertEqual(find_max_product([1, 2, 3, 0, 4, 2]), 8)
        self.assertEqual(find_max_product([0]), 0)
        self.assertEqual(find_max_product([]), 0)
        self.assertEqual(find_max_product([-2, -2, 0, -5, -1]), 5)
        self.assertEqual(find_max_product([-2, -3, 0, -4, -1]), 6)
        self.assertEqual(find_max_product([-2, -2, 0, -3, -1, -2]), 4)
        self.assertEqual(find_max_product([-2, -2, -2, 0, -3, -2, -2]), 6)
        self.assertEqual(find_max_product([-2, -2, 0, -3, -1, -2]), 4)

    def test_extreme(self):
        n = 10000
        self.assertEqual(find_max_product([2, 3] * n), 6 ** n)
        self.assertEqual(find_max_product([-2, -3] * n), 6 ** n)
        self.assertEqual(find_max_product([-2, 3] * n), 6 ** n)
        self.assertEqual(find_max_product([-7] + [-2, 3] * n), 7 * 6 ** (n - 1))
        self.assertEqual(find_max_product([-2, 3] * n + [-7]), 7 * 3 * 6 ** (n - 1))

        n = 10001
        self.assertEqual(find_max_product([2, 3] * n), 6 ** n)
        self.assertEqual(find_max_product([-2, -3] * n), 6 ** n)
        self.assertEqual(find_max_product([-2, 3] * n), 3 * 6 ** (n - 1))
        self.assertEqual(find_max_product([-7] + [-2, 3] * n), 7 * 6 ** n)
        self.assertEqual(find_max_product([-2, 3] * n + [-7]), 7 * 6 ** n)

if __name__ == '__main__':
    unittest.main()