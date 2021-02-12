class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        c1 = {}
        c2 = {}
        i = 0
        j = -1
        k = -1
        ans = 0
        for i, x in enumerate(A):
            c1[x] = c1.get(x, 0) + 1
            c2[x] = c2.get(x, 0) + 1
            if len(c1) < K:
                continue
            while j+1 < n and len(c1) > K:
                j += 1
                c1[A[j]] -= 1
                if not c1[A[j]]:
                    del c1[A[j]]
            while k < j or k < i and k+1 < n and c2[A[k+1]] > 1:
                k += 1
                c2[A[k]] -= 1
                if not c2[A[k]]:
                    del c2[A[k]]
            ans += k-j+1
        return ans
