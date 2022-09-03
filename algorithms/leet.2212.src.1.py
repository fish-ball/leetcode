class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = numArrows
        ans = 0
        v = [0,0,0,0,0,0,0,0,0,0,n]
        for mask in range(1 << 12):
            rem = n
            cnt = 0
            vv = []
            # ii = []
            for i in range(12):
                if (1<<i) & mask:
                    k = aliceArrows[i] + 1
                    rem -= k
                    cnt += i
                    # ii.append(f'i={i}, k={k}, rem={rem}, cnt={cnt}')
                    vv.append(k)
                else:
                    vv.append(0)
            if rem >= 0 and cnt > ans:
                # print(v, cnt, rem)
                # for r in ii: print(r)
                vv[0] += rem
                ans = cnt
                v = vv
        return v
