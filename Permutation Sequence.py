class Solution:
    # @return a string
    def getPermutation(self, n, k):
        strs = [] #store each digits by order
        available = list(range(1,n+1)) #store still available digits
        d = n #indicating which digit we are processing
        index = k-1 #k strats from 1, we want to start from 0
        while d > 0:
            for i in range(0,d):
                if i*self.factorial(d-1) <= index < (i+1)*self.factorial(d-1): #decide current digit
                    strs.append(str(available[i])) #store this digit
                    available.remove(available[i]) #this digit is no longer available
                    index = index%self.factorial(d-1) # narrow the search range
            d -= 1
        return "".join(strs)
        
    def factorial(self,n):
        if n==0:
            return 1
        else:
            return n*self.factorial(n-1)