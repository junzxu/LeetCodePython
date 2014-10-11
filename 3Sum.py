class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if not num:
            return []
        res = []
        visited = []
        cache = {}
        num.sort()
        for i in range(0,len(num)):
            if num[i] in visited:
                #we cover all pairs with num[i] as first value before
                continue
            if num[i] > 0:
                # all the values will be greater than 0 afterwards 
                break
            cache = {}
            duplicates = [] #deal with duplicate pairs
            visited.append(num[i])
            for j in range(i+1,len(num)):
                if cache.has_key(num[j]) and num[j] not in duplicates:
                    pair = cache[num[j]] + [num[j]]
                    res.append(pair)
                    duplicates.append(num[j])
                else:
                    cache[-num[i]-num[j]] = [num[i],num[j]]
                    
        return res