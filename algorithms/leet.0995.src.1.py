from collections import deque

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        acc = 0
        D = deque()
        for i in range(N):
            c = A[i]
            while D and D[0] <= i - K:
                D.popleft()
            if not (c ^ (len(D) & 1)):
                if i > N-K:
                    return -1
                acc += 1
                D.append(i)
        return acc
