def max_profit_any(prices):
    cash_not_owning_share = 0
    cash_owning_share = -float('inf')

    for price in prices:
        # States:
        # 1) owning share cash states:
        buy  = cash_not_owning_share - price
        hold = cash_owning_share

        # 2) not owning share cash states:
        sell = cash_owning_share + price
        save = cash_not_owning_share

        cash_not_owning_share = max(save, sell)
        cash_owning_share = max(buy, hold)

    return cash_not_owning_share

def max_profit_buget(prices, buget):
    cash_not_owning_share = buget
    cash_owning_share = -float('inf')

    for price in prices:
        # States:
        # 1) owning share cash states:
        buy  = cash_not_owning_share - price
        hold = cash_owning_share

        # 2) not owning share cash states:
        sell = cash_owning_share + price
        save = cash_not_owning_share
        cash_not_owning_share = max(save, sell)

        cash_owning_share = max(buy, hold)
        if cash_owning_share < 0:
            cash_owning_share = -float('inf')

    return cash_not_owning_share

def max_profit_limit(prices, limit):
    # each number of transaction has it's own pair of
    # cash_not_owning_share and cash_owning_share values
    # On start there are 0 transactions so the number
    # of pairs is limit + 1.
    cash_not_owning_share = [-float('inf')] * (limit + 1)
    cash_not_owning_share[0] = 0

    cash_owning_share = [-float('inf')] * (limit + 1)

    for price in prices:
        for transaction in range(limit):
            # States:
            # 1) owning share cash states:
            buy  = cash_not_owning_share[transaction] - price
            hold = cash_owning_share[transaction]

            # 2) not owning share cash states:
            sell = cash_owning_share[transaction] + price

            # selling a share means that must compare with next state
            # since we completed a transaction
            if transaction < limit:
                cash_not_owning_share[transaction + 1] = max(cash_not_owning_share[transaction + 1], sell)

            cash_owning_share[transaction] = max(buy, hold)

    return max(cash_not_owning_share)

prices = []
with open("input.txt", 'r') as f:
    prices = [int(s) for s in f.readline().split(' ') if len(s) != 0]

print(f'{prices=}')
print("unlimit, max profit:", max_profit_any(prices))
buget=1
print(f'{buget=}, max profit:', max_profit_buget(prices, buget))
buget=0
print(f'{buget=}, max profit:', max_profit_buget(prices, buget))
limit=1
print(f'{limit=}, max profit:', max_profit_limit(prices, limit))
limit=2
print(f'{limit=}, max profit:', max_profit_limit(prices, limit))
limit=3
print(f'{limit=}, max profit:', max_profit_limit(prices, limit))
