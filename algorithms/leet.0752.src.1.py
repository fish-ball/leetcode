class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        b = [-1] * 10000
        b[0] = 0
        for c in deadends:
            b[int(c)] = -2
        q = Deque([0])
        while q:
            x = q.popleft()
            #print(f'{x:04d} {b[x]}')
            if f'{x:04d}' == target:
                return b[x]
            d = [x//10**i%10 for i in range(4)]
            for i, a in enumerate(d):
                d[i] += 9
                d[i] %= 10
                y = sum(d[j]*(10**j) for j in range(4))
                if b[y] == -1:
                    b[y] = b[x] + 1
                    q.append(y)
                d[i] += 2
                d[i] %= 10
                y = sum(d[j]*(10**j) for j in range(4))
                if b[y] == -1:
                    b[y] = b[x] + 1
                    q.append(y)
                d[i] += 9
                d[i] %= 10
                y = sum(d[j]*(10**j) for j in range(4))
        return -1
