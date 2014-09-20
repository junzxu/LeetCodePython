class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        cache = {} #store all value we visited as key, the longest consecutive range as value
        longest = 0
        for number in num:
            if cache.has_key(number):
                continue
            lo = number
            hi = number
            if cache.has_key(number-1):
                lo = cache[number-1][0]
            if cache.has_key(number+1):
                hi = cache[number+1][1]
            longest = max(longest, hi-lo+1)
            cache[number] = [lo,hi]
            cache[lo] = [lo,hi]
            cache[hi] = [lo,hi]
        return longest