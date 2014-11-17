class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num:
            return []
    	i = j = -1
    	for k in range(0,len(num)-1):
    		if num[k] < num[k+1]:
    			i = k
    	if i == -1: return num[::-1]
    	for k in range(i+1, len(num)):
    		if num[i] < num[k]:
    			j = k
    	num[i], num[j] = num[j], num[i]
    	next = num[:i+1] + sorted(num[i+1:])
    	return next