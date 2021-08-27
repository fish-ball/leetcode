class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n = 0
        self.q1 = [99999999]
        self.q2 = [99999999]


    def addNum(self, num: int) -> None:
        self.n += 1
        if self.n % 2:
            a = heapq.heappop(self.q1)
            b = heapq.heappop(self.q2)
            a, b, c = sorted([-a, b, num])
            heapq.heappush(self.q1, -a)
            heapq.heappush(self.q1, -b)
            heapq.heappush(self.q2, c)
        else:
            a = heapq.heappop(self.q1)
            a, b = sorted([-a, num])
            heapq.heappush(self.q1, -a)
            heapq.heappush(self.q2, b)

    def findMedian(self) -> float:
        return -self.q1[0] if self.n % 2 else 0.5 * (self.q2[0] - self.q1[0])

