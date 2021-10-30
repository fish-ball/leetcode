class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(lambda x,y: x^y, nums, 0)
        k = x&(~x)+1
        a1 = reduce(lambda x,y: x^y, [a for a in nums if a&k], 0)
        a2 = reduce(lambda x,y: x^y, [a for a in nums if not(a&k)], 0)
        return [a1, a2]
