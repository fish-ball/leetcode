class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[-1 if i else 0] * n for i in range(target)]
        # k: 第几间房子
        # i: 当前的街区数
        # j: 房子的颜色
        for k in range(m):
            # print(f'house{k}:')
            dp2 = [[-1] * n for i in range(target)]
            for i in range(target-1, -1, -1):
                for j in range(n):
                    # j: 上一个房子的颜色
                    if dp[i][j] == -1:
                        continue
                    for jj in [houses[k]-1] if houses[k] else range(n):
                        # jj: 新一个房子的颜色
                        new_cost = 0 if houses[k] else cost[k][jj]
                        ii = i if j == jj or not k else i+1
                        if ii >= target:
                            continue
                        if dp2[ii][jj] == -1 \
                                or dp2[ii][jj] > dp[i][j] + new_cost:
                            dp2[ii][jj] = dp[i][j] + new_cost
            # for row in dp2:
            #     print('  ', row)
            dp = dp2
        results = [x for x in dp[-1] if x > -1]
        return min(results) if results else -1
