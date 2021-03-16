import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        hp = []
        for a, b in classes:
            heapq.heappush(hp, (a/b-(a+1)/(b+1), a, b))
        for i in range(extraStudents):
            r, a, b = heapq.heappop(hp)
            heapq.heappush(hp, ((a+1)/(b+1)-(a+2)/(b+2), a+1, b+1))
        return sum([a/b for r, a, b in hp]) / len(hp)
            
