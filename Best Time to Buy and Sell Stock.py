class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        Lowest = [prices[0]] #store the lowest price seen before day i
        for i in range(1,len(prices)):
            Lowest.append(min(Lowest[i-1],prices[i]))
        Max_profit = 0   #max profit should always great or equal than 0
        for i in range(1,len(prices)):
            profit = prices[i]-Lowest[i]
            Max_profit = max(Max_profit,profit)
        return Max_profit