class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = [0]
        for x in arr:
            acc.append(acc[-1] ^ x)
        return [acc[j+1]^acc[i] for i, j in queries]
