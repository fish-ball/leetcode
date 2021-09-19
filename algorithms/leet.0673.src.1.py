class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        stk = []
        kk = []
        for x in nums:
            k = bisect.bisect_left(stk, Deque([[x]]))
            # print(f'push: {x}, k = {k}')
            if k > 0 and stk[k-1]:
                # print(f'  pop..{stk[k-1]}')
                while stk[k-1][-1][0] >= x:
                    _, dec = stk[k-1].pop()
                    kk[k-1] -= dec
            if k == len(stk):
                cnt = kk[-1] if kk else 1
                stk.append(Deque([[x, cnt]]))
                kk.append(cnt)
            elif k >= 0:
                cnt = kk[k-1] if k > 0 else 1
                if stk[k][0][0] == x:
                    stk[k][0][1] += cnt
                    kk[k] += cnt
                else:
                    stk[k].appendleft([x, cnt])
                    kk[k] += cnt
            # for row in stk:
            #     print(row)
            # print(f'kk:  {kk}')
        return kk[-1]
