class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums)//2
        nums.sort()
        # print()
        # print(nums)
        for i in range(1, n+n):
            d = nums[i]-nums[0]
            if d == 0 or d % 2 == 1:
                continue
            hp = nums[:]
            heapq.heapify(hp)
            s0 = dict(Counter(nums))
            ss = dict()
            ok = True
            # print(f'd = {d}')
            ans = []
            while s0:
                while hp[0] in ss:
                    x = heapq.heappop(hp)
                    ss[x] -= 1
                    if not ss[x]:
                        del ss[x]
                x = heappop(hp)
                ans.append(x+d//2)
                s0[x] -= 1
                if not s0[x]:
                    del s0[x]
                xx = x + d
                if xx not in s0:
                    ok = False
                    break
                s0[xx] -= 1
                if s0[xx] == 0:
                    del s0[xx]
                ss[xx] = ss.get(xx, 0) + 1
                # print(s0, ss)
                # print(hp, ans)
            if ok:
                return ans
            
                
                
