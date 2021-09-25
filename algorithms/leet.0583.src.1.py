class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        a = [0] * (n+1)
        for x in word1:
            for j in range(n, 0, -1):
                if x == word2[j-1]:
                    a[j] = max(a[j], a[j-1] + 1)
            for i in range(n):
                a[i+1] = max(a[i], a[i+1])
            # print(a)
        return m + n - 2 * max(a)
