# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days. The following guidelines need
# to be followed:
#
# We can buy and sell the stock any number of times.
# In order to sell the stock, we need to first buy it on the same or any previous day.
# We can’t buy a stock again after buying it once. In other words, we first buy a stock and then sell it. After selling
# we can buy and sell again. But we can’t sell before buying and can’t buy before selling any previously bought stock.

# ex-> a = [7,1,5,3,6, 4] => buy(1)-> sell(5) => profit = 4 , buy(3) -> sell(6)=3
# time = O(n*n)
# Space = O(1)

def buySell(buy, stock):
    n = len(stock)
    ahead = [0 for _ in range(2)]
    curr = [0 for _ in range(2)]

    # if ind == n: return 0  # base case covered in assign 0 to dp
    for ind in range(n - 1, -1, -1):
        for buy in range(0, 2):
            if buy == 0:
                curr[buy] = max(-stock[ind] + ahead[1], ahead[0])
            else:  # sell the stock
                curr[buy] = max(stock[ind] + ahead[0], ahead[1])
        ahead = curr[:]
    return ahead[0]


stock = [7, 1, 5, 3, 6, 4]
n = len(stock)
print(buySell(0, stock))
