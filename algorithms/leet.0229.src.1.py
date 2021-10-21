class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = None
        ax = 0
        b = None
        bx = 0
        for x in nums:
            if x == a or a is None:
                a = x
                ax += 1
            elif x == b or b is None:
                b = x
                bx += 1
                if bx > ax:
                    a, b = b, a
                    ax, bx = bx, ax
            else:
                ax -= 1
                if ax <= 0:
                    a = None
                    ax = 0
                bx -= 1
                if bx <= 0:
                    b = None
                    bx = 0
            # print(a, ax, b, bx)
        ax = 0
        bx = 0
        for x in nums:
            if x == a:
                ax += 1
            if x == b:
                bx += 1
        ans = []
        if ax > len(nums) // 3:
            ans.append(a)
        if bx > len(nums) // 3:
            ans.append(b)
        return ans
