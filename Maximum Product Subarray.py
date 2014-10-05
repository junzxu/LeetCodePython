class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return 0
        Max = float('-Inf') #max product
        product = 1 #keep the cumulative product
        for i in range(0,len(A)): #forward pass
            product *= A[i]
            Max = max(Max,product)
            if abs(product) < 1:
                product = 1

        product = 1
        for i in range(len(A)-1,-1,-1): #backward pass
            product *= A[i]
            Max = max(Max,product)
            if abs(product) < 1:
                product = 1
                
        return Max