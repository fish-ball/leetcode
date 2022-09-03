class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = dict(Counter(nums))
        ans = []
        for x, n in d.items():
            if n == 1 and x-1 not in d and x+1 not in d:
                ans.append(x)
        return ans
        
