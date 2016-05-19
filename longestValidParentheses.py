class Solution(object):
    def longestValidParentheses(self,s):
    	"""
    	:type s: str
    	:rtype: int
    	"""
    	longest = 0
    	offset = 0
    	stack = []
    	for i,c in enumerate(s):
    		if c == '(':
    			stack.append(('(', i))
    		elif c == ')':
    			if len(stack) > 0:
    				match = stack.pop()
    				if len(stack) == 0:
    					longest = max(longest, i-offset+1)
    				else:
    					longest = max(longest, i-stack[-1][1])
    			else:
    				offset = i + 1
    				stack = []
    		else:
    			stack = []
    	return longest
