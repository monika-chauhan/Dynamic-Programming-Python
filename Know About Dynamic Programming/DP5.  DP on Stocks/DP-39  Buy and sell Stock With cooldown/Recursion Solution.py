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

def buySell(ind, buy, stock):
    n = len(stock)
    if ind >= n:
        return 0
    if buy == 0:
        donBuy = 0 + buySell(ind + 1, 0, stock)
        doBuy = -stock[ind] + buySell(ind + 1, 1, stock)
        return max(donBuy, doBuy)
    else:
        donSell = 0 + buySell(ind + 1, 1, stock)
        doSell = stock[ind] + buySell(ind + 2, 0, stock)
        return max(donSell, doSell)

stock = [4, 9, 0, 4, 10]
print(buySell(0, 0, stock))

