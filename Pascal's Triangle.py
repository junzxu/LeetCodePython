class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        triangle = [[] for i in range(0,numRows)]
        triangle[0].append(1)
        for i in range(1, numRows):
            triangle[i].append(1)
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle[i].append(1)
        return triangle