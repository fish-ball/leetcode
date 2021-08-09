class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [y for x, y in sorted([(sum(r), i) for i, r in enumerate(mat)])[:k]]
