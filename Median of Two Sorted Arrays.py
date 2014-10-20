class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if not A and not B:
            return None
        elif not A:
            return self.median(B)
        elif not B:
            return self.median(A)
        if len(A)+len(B) <= 4:
            C = A + B
            C.sort()
            return self.median(C)

        #the median of A+B is between median_A and median_B, we make median_A always less than median_B,
        #so we exclude values < median_A or values > median_B each recursion
        mid_A = self.median(A)
        mid_B = self.median(B)
        if mid_A == mid_B:
            return mid_A
        elif mid_A > mid_B:
            mid_A,mid_B = mid_B,mid_A
            A,B = B,A
        
        countA = (len(A)-1)/2 #number of values less than mid_A
        countB = (len(B)-1)/2  #number of values greater than mid_B
        if countA > countB:
            count = countA
            k = len(A)-1
            j = len(B)-1
            while count > 0:
                if j>=0 and B[j] >= A[k]:
                    j -= 1
                    count -=1
                else:
                    k -= 1
                    count -= 1
            return self.findMedianSortedArrays(A[(len(A)-1)/2:k+1],B[:j+1])
        else:
            count = countB
            k = 0
            j = 0
            while count > 0:
                if j < len(A) and A[j] < B[k]:
                    j += 1
                    count -=1
                else:
                    k += 1
                    count -= 1
            return self.findMedianSortedArrays(A[j:],B[k:1+len(B)/2])
    
    def median(self,A):
        return A[(len(A)-1)/2] if len(A)%2 != 0 else 0.5*(A[(len(A)-1)/2]+A[len(A)/2])
        