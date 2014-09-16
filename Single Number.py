class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        cache = {}
        for elem in A:
            if not cache.has_key(elem):
                cache[elem] = 1
            else:
                del cache[elem]
        number = cache.keys()
        return number[0]