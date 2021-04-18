class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        q = []
        t = 0
        for i, a in enumerate(tasks):
            a.append(i)
        tasks.sort(reverse=True)
        while tasks or q:
            if q:
                pt, i = heapq.heappop(q)
                ans.append(i)
                t += pt
            elif t < tasks[-1][0]:
                t = tasks[-1][0]
            while tasks and t >= tasks[-1][0]:
                et, pt, i = tasks.pop()
                heapq.heappush(q, (pt, i))
        return ans
