# Definition for a point
# import math
# from itertools import combinations
 
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        
 
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        maxNum = 0 #result
        for i in range(0,len(points)):
            visited = {} #visited points
            number = 0  #points have same coordinates with current point
            p1 = points[i]
            for j in range(i+1,len(points)):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    number += 1
                    continue
                if p1.y == p2.y:
                    slope = float('Inf')
                else:
                    slope = (1.0*(p1.x-p2.x))/(p1.y-p2.y)
                visited[slope] = visited.get(slope,0) + 1 #count number of line with same slope
            if len(visited) > 0:
                Num = 1 + number + max([v for (k,v) in visited.iteritems()])
            else:
                Num = 1+number
            if Num > maxNum:
                maxNum = Num
        return maxNum
