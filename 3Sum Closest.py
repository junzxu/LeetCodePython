class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        closest = sum(num[0:3])
        for i in range(0, len(num)-2):
            j = i + 1 #second num
            k = len(num) - 1 #third number
            while j < k:
                Sum = num[i] + num[j] + num[k]
                if abs(target - closest) > abs(target - Sum):
                    closest = Sum
                    if (closest == target): return closest
                if Sum > target:
                    k-=1
                else:
                    j+=1

        return closest