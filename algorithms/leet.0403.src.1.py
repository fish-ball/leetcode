class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        last = stones[-1]
        idx = dict([(x, i) for i, x in enumerate(stones)])
        dp = dict()
        def dfs(i, k):
            # print(f'dfs({i}, {k})')
            if i == n - 1:
                return True
            if (i, k) in dp:
                return dp[(i, k)]
            for kk in (k+1, k, k-1):
                if kk > 0 and stones[i] + kk in idx \
                        and dfs(idx[stones[i] + kk], kk):
                    # dp[(i, k)] = True
                    # print(f'dp[({stones[i]}, {k})] = {dp[(i, k)]}')
                    return True
            dp[(i, k)] = False
            # print(f'dp[({stones[i]}, {k})] = {dp[(i, k)]}')
            return False
        return dfs(0, 0)
        
