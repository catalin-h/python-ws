from collections import deque
from functools import lru_cache

amount = 0
coins = []

with open('input.txt', 'r') as f:
    amount = int(f.readline())
    coins = [int(x) for x in f.readline().split(' ') if x.isdecimal()]

# Sort coins in ascending order to reach the solution faster
coins = sorted(coins, reverse=False)

print(f'{amount=}')
print(f'{coins=}')

def coins_change(amount, coins):
    # holds the intermediary solutions
    solutions = {0: []}

    # the amounts to be processed next and
    # generate new amounts and possible solutions
    subtotals_q = deque([0])

    while subtotals_q:
        subtotal = subtotals_q.popleft()

        for coin in coins:
            next_subtotal = subtotal + coin
            if next_subtotal > amount:
                continue
            elif next_subtotal == amount:
                print("len(solutions)=", len(solutions))
                print("len(subtotals_q)=", len(subtotals_q))
                return solutions[subtotal] + [coin]
            elif next_subtotal not in solutions:
                solutions[next_subtotal] = solutions[subtotal] + [coin]
                # Design choice to limit the memory and the iterations count:
                # use LIFO in order to process the closest subtotal to the
                # amount _first_. This is still a BFS search as we consume
                # the entire subtotals queue.
                # eg. amount=1273 and coins=[1, 5, 10, 20, 50, 100, 200, 500]
                # len(solutions)= 35 and len(subtotals_q)= 27
                # vs poping at the other end:
                # len(solutions)= 1093 and len(subtotals_q)= 244
                subtotals_q.appendleft(next_subtotal)

    return None

print('change:', coins_change(amount, coins))

# O(N*V)
def coins_change_all_ways(amount, coins):

    @lru_cache(maxsize=None)
    def helper(amount):
        if amount < 0:
            return 0

        if amount == 0:
            return 1

        ways = 0

        for coin in coins:
            ways += helper(amount - coin)

        return ways

    return helper(amount)

def count_ways_to_pay(coins, amount):
    @lru_cache
    def helper(amount):
        # Nothing more left to pay: a single way.
        if amount == 0:
            return 1
        # Invalid payment: we paid too much so the amount that
        # remains is negative.
        if amount < 0:
            return 0
        num_ways = 0
        # Consider all the possible ways to choose the first coin:
        for first in coins:
            # Count the ways to pay the rest of the amount.
            num_ways += helper(amount - first)
        return num_ways
    return helper(amount)

def coins_change_all_ways2(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for amt in range(amount):
        for coin in coins:
            next = amt + coin
            if next > amount:
                continue
            dp[next] += dp[amt]
    return dp[amount]

print('count all ways:', count_ways_to_pay(coins, amount))
print('change all ways:', coins_change_all_ways(amount, coins))
print('change all ways iter:', coins_change_all_ways2(amount, coins))

# O(N*V)
def coins_change_all_unique_ways_rec(amount, coins):

    @lru_cache(maxsize=None)
    def helper(cindex, amount):
        # This condition must be first checked since we
        # can reach past the last coin but the amount left
        # to pay is 0
        if amount == 0:
            return 1

        if cindex == len(coins) or amount < 0:
            return 0

        ways = 0
        coin = coins[cindex]

        for count in range(amount // coin + 1):
            amt = coin * count
            ways += helper(cindex + 1, amount - amt)

        return ways

    return helper(0, amount)

def coins_change_all_unique_ways_iter(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for amt in range(amount):
            next = amt + coin

            if next > amount:
                continue

            dp[next] += dp[amt]

    return dp[amount]

print('change all unique ways recursive:', coins_change_all_unique_ways_rec(amount, coins))
print('change all unique ways iter:', coins_change_all_unique_ways_iter(amount, coins))
