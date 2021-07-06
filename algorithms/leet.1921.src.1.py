class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        k = 0
        for x in sorted((d-1)//s+1 for d, s in zip(dist, speed)):
            # print(x)
            if x <= k:
                break
            k += 1
        return k
