class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        s = set((1, 0))
        q = Deque([(0, (1, 0))])
        while q:
            k, (x, p) = q.popleft()
            # print(k, (x, p))
            for xx, pp in [(x+p, p), (x, x)]:
                if (xx, pp) in s or xx > n:
                    continue
                if xx == n:
                    return k+1
                s.add((xx, pp))
                q.append((k+1, (xx, pp)))

