class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not newInterval:
            return intervals
        i = 0
        while i<len(intervals):
            #find all intervals that may intersect
            if intervals[i].start <= newInterval.end:
                if intervals[i].end >= newInterval.start:
                    interval = intervals.pop(i)
                    newInterval.start = min(interval.start, newInterval.start)
                    newInterval.end = max(interval.end, newInterval.end)
                else:
                    i += 1
            #no intersections could be found
            else:
                break
        
        #insert the new interval
        intervals.insert(i, newInterval)
        return intervals