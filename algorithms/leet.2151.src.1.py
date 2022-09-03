class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        for mask in range(1<<n):
            k = bin(mask).count('1')
            if k < ans:
                continue
            yes = True
            for i in range(n):
                # 如果 i 是个坏人，不存在矛盾
                if ((1<<i) & mask) == 0:
                    continue
                for j in range(n):
                    # 如果 i 是好人，但是他说错了
                    if statements[i][j] == 0 and ((1<<j)&mask) \
                            or statements[i][j] == 1 and not ((1<<j)&mask):
                        yes = False
                        break
                if not yes:
                    break
            if yes:
                ans = k
        return ans
