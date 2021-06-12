class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ans = 0
        dp = {(0, 0): [0]}
        q = deque([(0, 0), (-1, -1)])
        for s in strs:
            print(q)
            c0 = s.count('0')
            c1 = s.count('1')
            while True:
                a0, a1 = q.popleft()
                if a0 == -1:
                    q.append((-1, -1))
                    break
                if a0 + c0 > m or a1 + c1 > n:
                    continue
                x = dp[(a0, a1)][0]
                q.append((a0, a1))
                if (a0+c0, a1+c1) not in dp:
                    dp[(a0+c0, a1+c1)] = [0]
                    q.append((a0+c0, a1+c1))
                y = dp[(a0+c0, a1+c1)]
                y[0] = max(y[0], x + 1)
                ans = max(ans, y[0])
            print((c0, c1), ans)
        return ans
