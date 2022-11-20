import collections
import unittest

# Note: process index within the sentence rather than actual string

def split_sentence(sentence: str, dictionary: list[str]) -> list[str]:
    """
    O(n*w), n = len(sentence), w = len(dictionary)
    """
    if not sentence:
        return []

    # Holds the splits or list of words up to some sentence index,
    # Note: the index represents the sentence[index:] range
    splits = {0 : []}

    # Holds next sentences indices, where each index represents the sentence[index:] range
    # Note: there can be multiple indices because there are derived words
    # e.g. fur and further or fury, and each one should be a candidate if
    # they are contained in the dictionary
    index_queue = collections.deque([0])

    while index_queue:
        index = index_queue.popleft()

        # Check which words match the start of the remaining sentence, that is sentence[:index]
        subsentence = sentence[index:]
        for word in dictionary:
            if not subsentence.startswith(word):
                continue

            next_index = index + len(word)

            # Note: avoid redundant work and add only unused indices
            if next_index in splits:
                continue

            splits[next_index] = splits[index] + [word]
            index_queue.append(next_index)

            if len(sentence) == next_index:
                return splits[next_index]

    return None

class TestSplits(unittest.TestCase):
    def test_normal(self):
        s = split_sentence("catseatmice", ["cat", "cats", "eat", "mice", "mouse"])
        self.assertEqual(s, ["cats", "eat", "mice"])

    def test_fail(self):
        s = split_sentence("", ["cat", "cats", "eat", "mice", "mouse"])
        self.assertEqual(s, [])
        self.assertEqual(split_sentence("carisfast", ["cat", "cats", "eat", "mice", "mouse"]), None)

if __name__ == '__main__':
    unittest.main()
