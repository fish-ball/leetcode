class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = []
        for i in range(1, n):
            heapq.heappush(q, (arr[0]/arr[i], 0, i))
        for t in range(k):
            f, i, j = heapq.heappop(q)
            if j > i + 1:
                heapq.heappush(q, (arr[i+1]/arr[j], i+1, j))
        return [arr[i], arr[j]]
