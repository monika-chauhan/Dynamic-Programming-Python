# We are given an array Arr[] of length n. It represents the price of a stock on ‘n’ days.
# The following guidelines need to be followed:

# We can buy and sell a stock only once.
# We can buy and sell the stock on any day but to sell the stock, we need to first buy it on the same or any
# previous day.
# We need to tell the maximum profit one can get by buying and selling this stock.

# Time Complexity: O(N)
# Reason: We are performing a single iteration
# Space Complexity: O(1)

def maxStockProfit(stock):
    maxProfit = 0
    mini = stock[0] # minimum price to buy a stock
    for i in range(1,len(stock)):
        currProfit = stock[i] - mini
        maxProfit = max(currProfit,maxProfit)
        mini = min(mini,stock[i]) # keep minimum 
    return maxProfit

stock = [7,1,5,3,6,4]
print("The maximum profit by selling the stock is ", maxStockProfit(stock))