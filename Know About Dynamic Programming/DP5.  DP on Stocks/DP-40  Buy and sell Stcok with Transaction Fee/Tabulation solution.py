# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days. The following guidelines need
# to be followed:
#
# We can buy and sell the stock any number of times.
# In order to sell the stock, we need to first buy it on the same or any previous day.
# We can’t buy a stock again after buying it once. In other words, we first buy a stock and then sell it. After selling
# we can buy and sell again. But we can’t sell before buying and can’t buy before selling any previously bought stock.
# After every transaction, there is a transaction fee (‘fee’) associated with it.
# Base case if ind == n: return 0
# explore all the possibility ->  One transaction charging a fee ->
# so once the one transaction completed means (buy and sell) then -> in selling deduct the transaction fee

# time = O(n*2)
# Space = O(n*2)


def buySell(stock, fee):
    n = len(stock)
    dp = [[0] * 2] * (n + 1)

    # if ind == n: return 0 # base case covered as assign 0 to dp
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            if buy == 0:
                donBuy = 0 + dp[ind + 1][0]
                doBuy = -stock[ind] + dp[ind + 1][1]
                dp[ind][buy] = max(donBuy, doBuy)

            else:
                donSell = 0 + dp[ind + 1][1]
                doSell = stock[ind] - fee + dp[ind + 1][0]
                dp[ind][buy] = max(donSell, doSell)
    return dp[0][0]


stock = [1, 3, 2, 8, 4, 9]
fee = 2
print(buySell(stock, 2))
