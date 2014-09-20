class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        length=len(s)
        is_palindrome=[[False for _ in xrange(length)] for _ in xrange(length)] #indicate if s[j:i] is palindrome
    
        for i in xrange(0,length):
          for j in xrange(0,i+1):
            if (s[j]==s[i])and((is_palindrome[j+1][i-1] if (i>0 and j<length-1 )else False) or i-j<2):
              is_palindrome[j][i]=True

        #DFS
        result = []
        stack = [[0]]
        while stack:
            indexes = stack.pop()
            if indexes[-1] == len(s):
                partial = self.reconstruct(s,indexes)
                result.append(partial)
            else:
                for i in range(indexes[-1], len(s)):
                    if is_palindrome[indexes[-1]][i] == True:
                        stack.append(indexes+[i+1])
        return result
        
    def reconstruct(self,s,indexes):
        #reconstruct palindrome list from indexes
        return [s[indexes[i]:indexes[i+1]] for i in range(0,len(indexes)-1)]