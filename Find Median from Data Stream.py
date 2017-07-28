class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxheap)== 0 or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap,num)
        if len(self.maxheap) - len(self.minheap) > 1:
            v = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -v)
        elif len(self.minheap) - len(self.maxheap) > 1:
            v = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -v)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if (len(self.maxheap) + len(self.minheap))%2 != 0:
            return -self.maxheap[0] if len(self.maxheap) > len(self.minheap) else self.minheap[0]
        else:
            return 1.0*(-self.maxheap[0] + self.minheap[0])/2
