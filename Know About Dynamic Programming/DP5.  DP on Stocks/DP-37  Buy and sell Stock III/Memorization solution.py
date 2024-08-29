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
# Space = O(n*2*3) + O(n)

def buySell(ind, buy, cap, stock):
    n = len(stock)
    dp = [[[-1]*(cap+1) for _ in range(2)] for _ in range(n+1)]

    if ind == n or cap == 0:
        return 0
    if dp[ind][buy][cap] != -1:
        return dp[ind][buy][cap]

    if buy == 1:
        doBuy = -stock[ind] + buySell(ind + 1, 0, cap, stock)
        donBuy = 0 + buySell(ind + 1, 1, cap, stock)
        dp[ind][buy][cap] = max(doBuy, donBuy)
        return dp[ind][buy][cap]
    else:
        doSell = stock[ind] + buySell(ind + 1, 1, cap - 1, stock)
        donSell = 0 + buySell(ind + 1, 0, cap, stock)
        dp[ind][buy][cap] = max(doSell, donSell)
        return dp[ind][buy][cap]

stock = [3, 3, 5, 0, 0, 3, 1, 4]
cap = 2
print(buySell(0, 1, cap, stock))
