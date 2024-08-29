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
# Space = O(n*2*3) 

def buySell(n, stock):
    dp = [[[0] * (3) for _ in range(2)] for _ in range(n + 1)]
    print(dp)
    # if ind == n or cap == 0: return 0 Base case covered

    for ind in range(n - 1, -1, -1):
        for buy in range(0, 2):
            for cap in range(1, 3):
                if buy == 0:
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][0][cap],-stock[ind] + dp[ind + 1][1][cap])
                else:
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][1][cap],stock[ind] + dp[ind + 1][0][cap - 1])
                print(dp)
    return dp[0][0][2]


stock = [1,2,3,4,5]
cap = 2
n = len(stock)
print(buySell(n, stock))
