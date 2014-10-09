class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        start = newInterval.start
        end = newInterval.end
        result = []
        found = False #indicating if we found the position of start point

        if start < intervals[0].start: #account for starts in left side of intervals
            result.append(Interval(start,end)) #the end value is not important here
            found = True
        for i in range(0,len(intervals)):
            if found == False: #check start position
                if intervals[i].start<=start<=intervals[i].end:
                    result.append(intervals[i])
                    found = True
                elif i-1>=0 and intervals[i-1].end<start<intervals[i].start:
                    result.append(Interval(start,end))
                    found = True
            if found == True: #check end position
                if intervals[i].start<=end<=intervals[i].end:
                    result[-1].end = intervals[i].end
                    found = False
                elif end < intervals[i].start:
                    result[-1].end = end
                    result.append(intervals[i])
                    found = False
                elif i == len(intervals)-1 and intervals[i].end < end:
                    result[-1].end = end
                    found = False                  
            else: #not interested region, add it to result
                result.append(intervals[i])

        if start > intervals[-1].end: #account for starts in right side of intervals
            result.append(newInterval)

        return result