class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        solutions = []
        stack = []
        for i in range(0,n):
            stack.append([(0,i)])
        
        #DFS
        while stack:
            solution = stack.pop()
            cols = [elem[1] for elem in solution]
            row = len(solution)
            if row == n:
                board = self.generateBoard(solution)
                solutions.append(board)
                continue
            for i in range(0,n):
                if not (i in cols) and self.safe(solution,(row,i)):
                    new_solution = solution + [(row,i)]
                    stack.append(new_solution)

        return solutions
    
                
    def safe(self,solution,loc):
        #check if location is safe
        rows = [elem[0] for elem in solution]
        cols = [elem[1] for elem in solution]
        diffs = [cols[i]-rows[i] for i in range(0,len(rows))]
        adds =  [cols[i]+rows[i] for i in range(0,len(rows))]

        if loc[0] in rows:
            return False
        if loc[1] in cols:
            return False
        if loc[1]-loc[0] in diffs or loc[0]+loc[1] in adds:
            return False
        return True
        
        
    def generateBoard(self,solution):
        #convert list of locations to list of strings
        n = len(solution)
        board = []
        for i in range(0,n):
            strs = ['.']*n
            col = solution[i][1]
            strs[col] = 'Q'
            row = "".join(strs)
            board.append(row)
        return board