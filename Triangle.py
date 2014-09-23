class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        layer = len(triangle)
        minpath = [0]*layer
        for i, elem in enumerate(triangle[-1]):
            minpath[i] = elem
        for k in range(layer-2,-1,-1):
            #from last row to first row
            for i in range(0,k+1):
                minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i] #sum at current row should be current value + minimum of two neighbor value at previous row
        return minpath[0]