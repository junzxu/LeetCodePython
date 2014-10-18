class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num:
            return []
        if len(num) == 1:
            return num
        if len(num) == 2:
            num[0],num[1] = num[1],num[0]
            return num
        
        num[1:] = self.nextPermutation(num[1:])
        if self.increasing(num[1:]):
            k = 1
            while k<len(num) and num[k] <= num[0]:
                k += 1
            if k != len(num):
                #replace the first digit with next larger digit
                num[0],num[k] = num[k],num[0]
            else:
                #put the first digit to the end
                val = num.pop(0)
                num.append(val)
            return num
        else:
            return num
    
    def increasing(self, li):
        for i in range(0,len(li)-1):
            if li[i]>li[i+1]:
                return False
        return True