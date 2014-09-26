class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        values = [1 for i in range(0, rowIndex+1)] #we only need the bottom row 
        for row in range(2, rowIndex+1):
            tmp = [elem for elem in values]
            for j in range(1, row):
                values[j] = tmp[j-1] + tmp[j]
        return values