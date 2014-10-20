class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        stack = [] #store all empty locations
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    stack.append((i,j))
        self.solve(board, stack)
    
    
    def solve(self,board, points):
        #DFS
        if self.win(board):
            return True
        i,j = points.pop()
        for k in range(1,10):
            if self.is_valid(board,i,j,str(k)):
                board[i][j] = str(k)
                if self.solve(board,points):
                    return True
                else:
                    board[i][j] = '.'
        points.append((i,j))
        return False

        
    def win(self,board):
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    return False
        return True
    
    def is_valid(self,board, i,j,k):
        #check value k is valid at location (i,j)
        for u in range(0,9):
            if board[i][u] != '.' and u != j and k == board[i][u]:
                return False
        for v in range(0,9):
            if board[v][j] != '.' and v != i and k == board[v][j]:
                return False
        offset_i = 3*(i//3)
        offset_j = 3*(j//3)
        for u in range(offset_i,offset_i+3):
            for v in range(offset_j,offset_j+3):
                if board[u][v] != '.' and (u!=i or v!=j) and k == board[u][v]:
                    return False
        return True