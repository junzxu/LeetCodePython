# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda x:x.start) #sort intervals by their start point
        i = 0
        while i<len(intervals)-1:
            if intervals[i+1].start <= intervals[i].end:
                intervals[i].end = max(intervals[i+1].end,intervals[i].end)
                intervals.pop(i+1)
            else:
                i+= 1
        return intervals