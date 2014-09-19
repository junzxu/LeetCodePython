class Solution:
    # @return a string
    def minWindow(self, S, T):
        Min = float("Inf")
        needed = {}  #number of each character in T
        captured = {} #number of each character in current window
        count = len(T) #number of characters the current window doesn't cover
        lower,upper = -1, len(S) #minimum length window indexs
        for char in T:
            needed[char] = needed.get(char,0)+1
        
        i,j = 0,0
        while i<len(S) and j<=len(S):
            if count>0 and j<len(S):
                captured[S[j]] = captured.get(S[j],0)+1
                if needed.has_key(S[j]) and captured[S[j]] <= needed[S[j]]:
                    count -= 1
                j = j+1
            elif count>0 and j==len(S):
                break
            else:
                if (j-i) < (upper-lower):
                    upper = j
                    lower = i
                if needed.has_key(S[i]) and captured[S[i]] <= needed[S[i]]:
                    count += 1
                captured[S[i]] -= 1
                i = i+1
                    
        if lower != -1:
            return S[lower:upper]
        else:
            return ""
            