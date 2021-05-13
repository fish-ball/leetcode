class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = dict()
        m = 1000000007
        def dfs(l, r, k):
            # print(' '*indent, f'>> dfs({l}, {r}, {k})')
            if k < l:
                return 0
            if k == 0 and l == 0:
                return 1
            ans = dp.get((l,r,k))
            if ans:
                return ans
            ans = dfs(l, r, k-1)
            if l > 0:
                ans += dfs(l-1, r+1, k-1)
            if r > 0:
                ans += dfs(l+1, r-1, k-1)
            ans %= m
            dp[(l,r,k)] = ans
            # print(' '*indent, f'<< dfs({l}, {r}, {k}) = {ans}')
            return ans
        
        return dfs(0, arrLen-1, steps)
