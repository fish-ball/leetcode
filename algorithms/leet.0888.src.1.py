from collections import Counter

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(B) - sum(A)) // 2
        cb = Counter(B)
        for x in sorted(Counter(A).keys()):
            if x + diff in cb:
                return [x, x+diff]
        return []

