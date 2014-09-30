class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        DP = [1]*(n+1) #Distinct ways to reach stair 0 to n, DP[0]=DP[1]=1
        for i in range(2,n+1):
            DP[i] = DP[i-1] + DP[i-2] #Could reach stair i from stair i-1 or i-2
        return DP[-1]