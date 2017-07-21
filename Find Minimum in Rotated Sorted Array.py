class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, nums):
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo)/2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
