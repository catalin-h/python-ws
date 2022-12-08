import unittest

# You are given a vector of integers numbers, and a list of queries of the form (start, end). For
# each query, you must compute the sum of the elements of numbers with indices in [start,
# end). Return the result as a list.
def range_query(numbers: list[int], queries: list[list[int]]) -> list[int]:
    if not numbers:
        return []

    prefix_sums = [0] * (len(numbers) + 1)
    for i, num in enumerate(numbers):
        prefix_sums[i + 1] = prefix_sums[i] + num

    results = [0] * len(queries)

    # Assume intervals are within bounds
    for i, (start, end) in enumerate(queries):
        results[i] = prefix_sums[end] - prefix_sums[start]

    return results

class Tests(unittest.TestCase):
    def test(self):
        n = 100
        numbers = [1] * n
        self.assertEqual(range_query(numbers, [[1,2], [0, n-1]]), [1, n - 1])

if __name__ == "__main__":
    unittest.main()