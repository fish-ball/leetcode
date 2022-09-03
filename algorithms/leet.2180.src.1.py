class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for x in range(2, num+1):
            yes = 1
            for c in str(x):
                if c in '13579':
                    yes ^= 1
            ans += yes
        return ans
                    
