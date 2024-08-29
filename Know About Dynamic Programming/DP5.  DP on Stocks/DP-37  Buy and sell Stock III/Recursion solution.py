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
# Cap  always be 2 only
def buySell(ind, buy, cap, stock):
    n = len(stock)
    if ind == n or cap == 0: return 0
    if buy == 0:
        doBuy = -stock[ind] + buySell(ind + 1, 1, cap, stock)
        donBuy = 0 + buySell(ind + 1, 0, cap, stock)
        return max(doBuy, donBuy)
    else:
        doSell = stock[ind] + buySell(ind + 1, 0, cap - 1, stock)
        donSell = 0 + buySell(ind + 1, 1, cap, stock)
        return max(doSell, donSell)


stock = [3, 3, 5, 0, 0, 3, 1, 4]
cap = 2
print(buySell(0, 0, cap, stock))
