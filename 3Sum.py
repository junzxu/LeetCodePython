class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if not num: return []
        res = []
        num.sort()
        for i,v1 in enumerate(num):
            if v1 > 0: break
            t = -v1
            if i>0 and v1 == num[i-1]: continue
            cache = {}
            for j,v2 in enumerate(num[i+1:]):
                if not cache.has_key(v2):
                    cache[t-v2] = 1
                elif cache[v2] > 1: continue
                else:
                    res.append([v1,t-v2,v2])
                    cache[v2] += 1
        return res