class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        Max_one = 0 #max profit made by one transaction
        lo = 0  #lower bound of onetrans range
        hi = 0  #upper bound of onetrans range
        lowest = 0 #lowest price index

        #first iteration, find the max profit made by one transaction and its range
        for i in range(1,len(prices)):
            if prices[i] <= prices[lowest]:
                lowest = i
            profit = prices[i]-prices[lowest]
            if profit > Max_one:
                Max_one = profit
                hi = i
                lo = lowest
                
        #second iteration, search for ranges outside the first transaction
        Max_two = max(self.oneTrans(prices[0:lo]), self.oneTrans(prices[hi+1:]))
        Max_total = Max_one + max(Max_two,0)
        
        #divide the first transactions
        first_trans = prices[lo+1:hi]
        new_total = Max_one + self.oneTrans(first_trans[::-1]) #new profit made by divide the first transaction
        Max_total = max(Max_total, new_total)
        return Max_total
        
    def oneTrans(self, prices):
        #max profit by making one transaction
        if len(prices) <= 1:
            return 0
        Lowest = [prices[0]]
        for i in range(1,len(prices)):
            Lowest.append(min(Lowest[i-1],prices[i]))
        Max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i]-Lowest[i]
            Max_profit = max(Max_profit,profit)
        return Max_profit