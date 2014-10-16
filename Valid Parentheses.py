class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return False
        Map = {}
        Map['{'] = '}'
        Map['('] = ')'
        Map['['] = ']'
        
        stack = []
        for i in range(0,len(s)):
            if len(stack) != 0 and not Map.has_key(s[i]):
                sign = stack.pop()
                if Map[sign] != s[i]:
                    return False
            elif Map.has_key(s[i]):
                stack.append(s[i])
            else:
                return False
        
        return len(stack)==0