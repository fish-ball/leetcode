class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        L = len(A)
        P = [False] * L
        for i in A:
            if 0 < i <= L:
                P[i-1] = True
        for i in range(L):
            if not P[i]:
                return i + 1
        return L + 1
        
