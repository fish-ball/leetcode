class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = dict()
        for a, b in edges:
            d[a] = d.get(a, 0) + 1
            d[b] = d.get(b, 0) + 1
            if d[a] > 1:
                return a
            if d[b] > 1:
                return b
        return -1
