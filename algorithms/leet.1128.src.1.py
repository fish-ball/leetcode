class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ct = dict()
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            ct[(a, b)] = ct.get((a, b), 0) + 1
        return sum([v*(v-1)//2 for v in ct.values()])
