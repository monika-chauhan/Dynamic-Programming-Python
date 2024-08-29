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

def stockProfit(stock):
    n = len(stock)
    cur = [0] * 2
    front1 = [0] * 2
    front2 = [0] * 2

    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            if buy == 0:
                donBuy = 0 + front1[0]
                doBuy = -stock[ind] + front1[1]
                cur[buy] = max(donBuy, doBuy)

            else:
                donSell = 0 + front1[1]
                doSell = stock[ind] + front2[0]
                cur[buy] = max(donSell, doSell)

        front2 = front1[:]
        front1 = cur[:]
    return cur[0]


prices = [4, 9, 0, 4, 10]
print("The maximum profit that can be generated is ", stockProfit(prices))
