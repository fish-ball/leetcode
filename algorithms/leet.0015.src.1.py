class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()
        ans = set()
        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                c = 0-a-b
                if c in s:
                    ans.add(tuple(sorted([a, b, c])))
            s.add(a)
        return [list(x) for x in ans]
