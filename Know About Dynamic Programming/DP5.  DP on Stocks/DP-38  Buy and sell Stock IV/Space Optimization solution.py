# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days. The following guidelines need
# to be followed:
# We can buy and sell the stock any number of times.
# In order to sell the stock, we need to first buy it on the same or any previous day.
# We can’t buy a stock again after buying it once. In other words, we first buy a stock and then sell it. After selling
# we can buy and sell again. But we can’t sell before buying and can’t buy before selling any previously bought stock.
# We can do at-most K transactions.
# Base case if ind == n or cap == 0: return 0
# After completed one Transaction means ( Buy and sell) then in sell decrease the (cap - 1)

# Time = O(n*2*3)
# space = O(k)


def buySell(cap, stock):
    n = len(stock)
    ahead = [[0] * (cap + 1) for _ in range(2)]
    curr = [[0] * (cap + 1) for _ in range(2)]

    # if ind == n or k == 0: return 0 # Base case covered as assign dp to  0
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            for k in range(1, cap + 1):
                if buy == 0:
                    doBuy = -stock[ind] + ahead[1][k]
                    donBuy = 0 + ahead[0][k]
                    curr[buy][k] = max(doBuy, donBuy)

                else:
                    doSell = stock[ind] + ahead[0][k - 1]
                    donSell = 0 + ahead[1][k]
                    curr[buy][k] = max(doSell, donSell)
        ahead = curr[:]
    return ahead[0][cap]


stock = [3, 3, 5, 0, 0, 3, 1, 4]
k = 2
print(buySell(2, stock))
