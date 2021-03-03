class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        m = 1
        for i in range(1, num+1):
            if (m << 1) <= i:
                m <<= 1
            ans.append(ans[i-m]+1)
        return ans
