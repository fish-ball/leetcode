from collections import deque

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        N = len(A)
        acc = 0
        D = deque()
        ans = 0
        for i in range(N):
            c = A[i]
            if not c:
                if not K:
                    acc = -1
                elif len(D) >= K:
                    j = D.popleft()
                    acc = i-j-1
                D.append(i)
            acc += 1
            ans = max(ans, acc)
        return ans
