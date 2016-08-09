class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            t = nums[i]
            if t <= 0 or t > len(nums) or t == i+1:
                i += 1
            else:
                if nums[t-1] != t:
                    nums[i] = nums[t-1]
                    nums[t-1] = t
                else:
                    i += 1
        for i in range(0,len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
