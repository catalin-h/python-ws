import unittest
import collections

def longest_increasing_subsequence(numbers: list[int]) -> list[int]:
    if not numbers:
        return []

    parents = [None] * len(numbers)
    max_paths = [1] * len(numbers)
    count = collections.Counter()

    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            # >= ensures that the sequence is monotonically increasing
            # whereas > does not
            if number >= numbers[j]:
                continue

            if max_paths[j] < max_paths[i] + 1:
                max_paths[j] = max_paths[i] + 1
                parents[j] = i
                count[j] += 1

    print(parents)
    print(max_paths)

    max_path_len = max(max_paths)
    max_index = max_paths.index(max_path_len)
    
    sequence = [numbers[max_index]]
    next = parents[max_index]

    while not next is None:
        sequence.append(numbers[next])
        next = parents[next]
    
    return sequence[::-1]

def longest_increasing_subsequences(numbers: list[int]) -> list[int]:
    if not numbers:
        return []

    parents = [None] * len(numbers)
    max_paths = [1] * len(numbers)
    count = [1] * len(numbers)

    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            # >= ensures that the sequence is monotonically increasing
            # whereas > does not
            if number >= numbers[j]:
                continue

            # Key feature: when a longer path is found override the
            # current element path count; when the length is the same
            # same then sum the two lengths.
            if max_paths[j] < max_paths[i] + 1:
                max_paths[j] = max_paths[i] + 1
                parents[j] = i
                # override current count as we found a longer path that ends
                # at current element
                count[j] = count[i]
            elif max_paths[j] == max_paths[i] + 1:
                # aggregate paths with same path length that ends at
                # current element
                count[j] += count[i]

    print(parents)
    print(max_paths)
    print(count)

    max_path_len = max(max_paths)
    max_index = max_paths.index(max_path_len)

    return count[max_index]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_increasing_subsequence([7, 1, 4, 3, 2, 1, 4, 5]), [1, 3, 4, 5])
        self.assertEqual(longest_increasing_subsequence([3, 2, 1]), [3])
        self.assertEqual(longest_increasing_subsequence([1, 3, 2]), [1, 3])
        self.assertEqual(longest_increasing_subsequence([1, 3]), [1, 3])
        self.assertEqual(longest_increasing_subsequence([2, 1]), [2])
        self.assertEqual(longest_increasing_subsequence([2]), [2])
        self.assertEqual(longest_increasing_subsequence([]), [])
    def test_count(self):
        #self.assertEqual(longest_increasing_subsequences([1, 4, 2, 1, 5]), 2)
        self.assertEqual(longest_increasing_subsequences([7, 1, 4, 3, 2, 1, 4, 5]), 2)

if __name__ == "__main__":
    unittest.main()