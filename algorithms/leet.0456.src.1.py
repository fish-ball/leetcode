class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        for x in nums:
            mn = min(x, stk[-1][0]) if stk else x
            while stk and stk[-1][0] < x:
                if x < stk[-1][1]:
                    return True
                stk.pop()
            stk.append([mn, x])
            # print(stk)
        return False
            
