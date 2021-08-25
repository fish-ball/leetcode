class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = Deque([[0]])
        ans = []
        while q:
            path = q.popleft()
            u = path[-1]
            for v in graph[u]:
                path2 = path + [v]
                if v == n-1:
                    ans.append(path2)
                else:
                    q.append(path2)
        return ans


