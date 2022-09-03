class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [x for x in nums if x > 0]
        b = [x for x in nums if x < 0]
        v = []
        for x, y in zip(a, b):
            v.append(x)
            v.append(y)
        return v
