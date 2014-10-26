class Solution:
	# @return a list of integers
	def getRow(self, rowIndex):
		values = [1 for i in range(0, rowIndex+1)] #we only need the bottom row 
		for row in range(1, rowIndex+1):
			values[row] = 1
			for col in range(row-1, 0, -1):
				values[col] = values[col-1] + values[col]
		return values