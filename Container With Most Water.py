class Solution:
    # @return an integer
    def maxArea(self, height):
        largest = 0
        i = 0
        j = len(height)-1
        while i < j:
            area = (j-i)*min(height[i],height[j])
            largest = max(largest,area)
            #each time we try to increase the smaller edge
            if height[i] <= height[j]:
                k = i
                while k < j and height[k] <= height[i]:
                    k += 1
                if k == j:
                    return largest
                i = k
            else:
                k = j
                while k >i and height[k] <= height[j]:
                    k -= 1
                if k == i:
                    return largest
                j = k                
            
        return largest