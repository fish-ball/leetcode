class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        x = 0
        for y in A:
            x *= 10
            x += y
        x += K
        ans = []
        while x:
            ans.append(x % 10)
            x //= 10
        return ans[::-1] or [0]
