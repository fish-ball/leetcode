class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1, 2]
        for i in range(64):
            fib.append(fib[-1] + fib[-2])
        bb = bin(n)[2:]
        # print(bb)
        last = False
        ans = 0
        for i, b in enumerate(bb):
            k = len(bb)-i-1
            if b == '0':
                last = False
                continue
            ans += fib[k]
            # print(i, b, ans)
            if last:
                break
            # print(f'k = {k}, fib[k] = {fib[k]}')
            last = True
        if '11' not in bb:
            ans += 1
        return ans
