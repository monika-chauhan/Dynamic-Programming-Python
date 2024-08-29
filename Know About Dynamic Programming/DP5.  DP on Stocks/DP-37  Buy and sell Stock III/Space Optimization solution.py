# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days. The following guidelines need
# to be followed:
#
# We can buy and sell the stock any number of times.
# In order to sell the stock, we need to first buy it on the same or any previous day.
# We can’t buy a stock again after buying it once. In other words, we first buy a stock and then sell it. After selling
# we can buy and sell again. But we can’t sell before buying and can’t buy before selling any previously bought stock.
# We can do at most 2 transactions.
# Base case if ind == n or cap == 0: return 0
# Possible all solution
# when the transaction completed means (b and sell) then decrease the cap in selling call

# time = O(n*2*3)
# Space = O(1)

def buySell(n, stock):
    ahead = [[0] * 3 for _ in range(2)]
    curr = [[0] * 3 for _ in range(2)]
    # dp = [[[0] * (3) for _ in range(2)] for _ in range(n + 1)]

    # if ind == n or cap == 0: return 0 Base case covered

    for ind in range(n - 1, -1, -1):
        for buy in range(0, 2):
            for cap in range(1, 3):
                if buy == 0:
                    curr[buy][cap] = max(0 + ahead[0][cap], -stock[ind] + ahead[1][cap])
                else:
                    curr[buy][cap] = max(0 + ahead[1][cap], stock[ind] + ahead[0][cap - 1])
        ahead = curr[:]
    return ahead[0][2]


stock = [3, 3, 5, 0, 0, 3, 1, 4]
cap = 2
n = len(stock)
print(buySell(n, stock))
