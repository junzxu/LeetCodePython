class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board is None or board == []:
            return
        
        row=len(board)
        if(row<3):return
        col=len(board[0])
        if(col<3):return
        
        #find all 'O's that is in the border
        for i in xrange(0,row):
            if board[i][0] == 'O':
                self.BFS(i,0,board)
            if board[i][col-1] == 'O':
                self.BFS(i,col-1,board)
                
        for j in xrange(0,col):
            if board[0][j] == 'O':
                self.BFS(0,j,board)
            if board[row-1][j] == 'O':
                self.BFS(row-1,j,board)
        
        #replace surrounded regions with 'x'
        for i in xrange(0,row):
            for j in xrange(0,col):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
                    
    def BFS(self,i,j,board):
        #search the neighbor of given position and set them to '_'
        board[i][j] = '1'
        queue = [(i,j)]
        while queue:
            (x,y) = queue.pop(0)
            for neighbor in self.neighbors(x,y,board):
                board[neighbor[0]][neighbor[1]] = '_'
                queue.append(neighbor)
    
    def neighbors(self, i,j,board):
        #return a list of neighbors which is 'O'
        row=len(board)
        col=len(board[0])
        li = []
        delta = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in delta:
            if i+dx < 0 or i+dx > row-1 or j+dy < 0 or j+dy > col-1:
                continue
            if board[i+dx][j+dy] == 'O':
                li.append((i+dx,j+dy))
        return li