class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        cum_sum = 0 #store the difference if total gas and cost
        minimum = float('Inf')
        min_station = -1
        for i in range(0, n):
            cum_sum += gas[i]-cost[i]
            if cum_sum < minimum:
                minimum = cum_sum
                min_station = (i+1)%n #we should start at the station with the lowest cumsum
        if cum_sum < 0:
            return -1
        else:
            return min_station