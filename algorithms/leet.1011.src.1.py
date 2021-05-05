class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # weights.sort(reverse=True)
        total = sum(weights)
        l = max(weights) - 1
        r = total
        n = len(weights)
        # print(weights)
        while l + 1 < r:
            m = l + r + 1 >> 1
            # print(l, m, r)
            q = 0
            d = 0
            for x in weights:
                if q + x <= m:
                    q += x
                else:
                    # print(f'q = {q}')
                    d += 1
                    q = x
            # print(f'q = {q}')
            d += 1
            # rem = total
            # d = 0
            # used = [0] * n
            # while rem > 0:
            #     pre = [-1] * (m + 1)
            #     pre[0] = -2
            #     for i, x in enumerate(weights):
            #         if used[i]:
            #             continue
            #         for j in range(m - x, -1, -1):
            #             if pre[j] != -1 and pre[j+x] == -1:
            #                 pre[j+x] = i
            #         print(f'  {x}:', [weights[k] if k > -1 else -1 for k in pre])
            #         if pre[m] != -1:
            #             break
            #     for j in range(m, -1, -1):
            #         if pre[j] > -1:
            #             rem -= j
            #             while j:
            #                 used[pre[j]] = 1
            #                 print(f'  pop: {weights[pre[j]]}')
            #                 j -= weights[pre[j]]
            #             break
            #     d += 1
            #     print(f'd = {d}/{D}, m = {m}')
            #     print(used)
            #     print([weights[k] if k > -1 else -1 for k in pre])
            #     if d > D:
            #         break
            # print(f'd = {d}/{D}, m = {m}')
            if d <= D:
                r = m
            else:
                l = m
        # print(l, r)
        return r
                

            
