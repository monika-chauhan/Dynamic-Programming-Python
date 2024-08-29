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

def buySell(ind, buy, stock, fee):
    n = len(stock)
    if ind == n: return 0
    if buy == 0:
        donBuy = 0 + buySell(ind + 1, 0, stock, fee)
        doBuy = -stock[ind] + buySell(ind + 1, 1, stock, fee)
        return max(donBuy, doBuy)
    else:
        donSell = 0 + buySell(ind + 1, 1, stock, fee)
        doSell = stock[ind] - fee + buySell(ind + 1, 0, stock, fee)
        return max(donSell, doSell)


stock = [1, 3, 2, 8, 4, 9]
fee = 2
print(buySell(0, 0, stock, 2))
