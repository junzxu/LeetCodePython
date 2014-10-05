class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(T) > len(S) or len(S) == 0 or len(T) == 0:
            return 0
        DP = []
        #init
        for i in range(0,len(T)+1):
            DP.append([])
            for j in range(0,len(S)+1):
                DP[i].append(0)
        for j in range(0,len(S)+1):
            DP[0][j] = 1 #first row is 1 because of empty set

        for i in range(1, len(T)+1):
            for j in range(i,len(S)+1):
                if T[i-1] == S[j-1]:
                    DP[i][j] =  DP[i-1][j-1] + DP[i][j-1]
                else:
                    DP[i][j] = DP[i][j-1]
        
        return max(DP[-1])