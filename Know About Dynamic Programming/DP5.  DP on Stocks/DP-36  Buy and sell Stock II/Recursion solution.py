# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days. The following guidelines need
# to be followed:
#
# We can buy and sell the stock any number of times.
# In order to sell the stock, we need to first buy it on the same or any previous day.
# We can’t buy a stock again after buying it once. In other words, we first buy a stock and then sell it. After selling
# we can buy and sell again. But we can’t sell before buying and can’t buy before selling any previously bought stock.

# ex-> a = [7,1,5,3,6, 4] => buy(1)-> sell(5) => profit = 4 , buy(3) -> sell(6)=3
# time = O(2^n)
# Space = O(n)

def buySell(ind, buy, stock):
    n = len(stock)
    if ind == n: return 0
    if buy == 0:
        profit = max(0 + buySell(ind + 1, 0, stock),-stock[ind] + buySell(ind + 1, 1, stock));
    else:  # sell the stock
        profit = max( 0 + buySell(ind + 1, 1, stock), stock[ind] + buySell(ind + 1, 0, stock),)
    return profit

stock = [7, 1, 5, 3, 6, 4]
n = len(stock)
print(buySell(0, 0, stock))
