class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        lo = 0
        hi = len(num)
        #binary search to find the largest element
        while lo<hi:
            mid = lo + (hi-lo)/2
            if num[mid] <= num[lo]:
                hi = mid
            else:
                lo = mid
        
        index = (lo+1)%len(num)
        return num[index]