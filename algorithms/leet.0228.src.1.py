class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        a = None
        b = None
        for x in nums + [None]:
            if a is None:
                a = x
                b = x
            elif x is not None and x - 1 == b:
                b = x
            elif b == a:
                ans.append(str(b))
                a = x
                b = x
            else:
                ans.append(f'{a}->{b}')
                a = x
                b = x
        return ans
