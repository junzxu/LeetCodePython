class Solution:
# @param grid, a list of lists of integers
# @return an integer
	def minPathSum(self, grid):
		if not grid:
			return 0
		row = len(grid)
		col = len(grid[0])
		DP = [[0]*col for j in range(0,row)]

		#init, because value is non-negative, so first row and col is the minimum path
		DP[0][0] = grid[0][0]
		for i in range(1,row):
			DP[i][0] = DP[i-1][0] + grid[i][0]
		for j in range(1,col):
			DP[0][j] = DP[0][j-1] + grid[0][j]

		#we can only move down or right, so we choose to move from a smaller path
		for i in range(1,row):
			for j in range(1,col):
				DP[i][j] = grid[i][j] + min(DP[i][j-1],DP[i-1][j])

		return DP[-1][-1]