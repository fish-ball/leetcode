class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        n = len(nums)
        for i, x in enumerate(nums):
            if x == key:
                for j in range(max(0, i-k), min(n,i+k+1)):
                    ans.add(j)
        return sorted(ans)
