class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxReach = 0 #indicating we can reach all the index i <= maxReach
        i = 0
        while i<len(A) and i<=maxReach:
            maxReach = max(i+A[i] ,canReach)
            if maxReach >= (len(A)-1):
                break
            i += 1
                    
        return maxReach >= (len(A)-1)