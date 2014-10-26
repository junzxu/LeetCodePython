class Solution:
    # @param num, a list of integer
    # @return an integer
	def findMin(self, num):
		hi = len(num)-1
		lo = 0
		while lo < hi:
			mid = lo + (hi-lo)/2
			if num[mid] == num[hi]:
				hi -= 1
			elif num[mid] < num[hi]: #right side sorted
				hi = mid
			else:
				lo = mid+1
		return num[lo]