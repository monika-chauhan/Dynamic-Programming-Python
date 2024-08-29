# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days. The following guidelines need
# to be followed:
#
# We can buy and sell the stock any number of times.
# In order to sell the stock, we need to first buy it on the same or any previous day.
# We can’t buy a stock again after buying it once. In other words, we first buy a stock and then sell it. After selling
# we can buy and sell again. But we can’t sell before buying and can’t buy before selling any previously bought stock.
# We can’t buy a stock on the very next day of selling it. This is the cooldown clause.
# Base case if ind == n : return 0
# Explore all possible stage -> if we buy(index1)  and sell (index2) then we can not buy on index3 so we can do one
# thing  We can move (ind + 2) in place of (ind+1) at the time of selling the stock so that it will not pick next day.

# time = O(n*2)
# Space = O(n*2)

def buySell(stock):
    n = len(stock)
    dp = [[0] * 2 for _ in range(n + 2)]
    # if ind >= n:  return 0 # Base case covered as assign 0
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            if buy == 0:
                donBuy = 0 + dp[ind + 1][0]
                doBuy = -stock[ind] + dp[ind + 1][1]
                dp[ind][buy] = max(donBuy, doBuy)

            else:
                donSell = 0 + dp[ind + 1][1]
                doSell = stock[ind] + dp[ind + 2][0]
                dp[ind][buy] = max(donSell, doSell)

    return dp[0][0]


stock = [4, 9, 0, 4, 10]
print(buySell(stock))
