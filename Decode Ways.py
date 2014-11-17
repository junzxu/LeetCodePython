class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s or s.startswith('0'):
            return 0
        cache = [0]*len(s)
        cache[0] = 1
        for i in range(1,len(s)):
            if s[i] != '0':
                cache[i] = cache[i-1]
            if 1 <= int(s[i-1:i+1]) <= 26 and not s[i-1:i+1].startswith('0'):
                cache[i] += cache[i-2] if i>2 else 1
        return cache[-1]