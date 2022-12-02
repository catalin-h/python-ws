import unittest

# Given a deck of cards, we have to deal a hand containing a certain number of cards. Cards
# can be dealt from the top of the deck as well as from the bottom. Determine the best hand
# that can be dealt, in terms of the sum of the values of the cards, assuming each card has a
# specific value.
# e.g. deck: [3, 1, 1, 6, 2], n = 3 => [3,1,1], [3,1,2], [2,6,1], [3,2,6] -> best: [3,2,6]
#
def best_cards(deck: list[int], size: int) -> int:
    deck_len = len(deck)
    if not deck or size == 0 or size > deck_len:
        return 0

    best = 0
    top_sum = 0
    bottom_sum = sum(deck[deck_len - size:])

    for top_card_index in range(size):
        best = max(best, top_sum + bottom_sum)

        # Increase the numbers of cards from top deck ...
        top_sum += deck[top_card_index]

        # ... on the other hand we decrease the number of cards
        # from bottom deck
        excluded_bottom_card_index = deck_len - size - top_card_index
        bottom_sum -= deck[excluded_bottom_card_index]

        print("include:", deck[top_card_index], "exclude:", deck[excluded_bottom_card_index])

    return best

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(best_cards([3, 1, 1, 6, 2], 3), 11)

if __name__ == "__main__":
    unittest.main()
