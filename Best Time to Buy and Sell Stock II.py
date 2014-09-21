class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        sum = 0
        for i in range(0,len(prices)-1):
            diff = prices[i+1] - prices[i]
            sum += max(0,diff) #we can do as many transactions as we want, so sell when the price is up
        return sum