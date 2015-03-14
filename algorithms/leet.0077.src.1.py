class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n < k or k < 0:
            return []
        if k == 0:
            return [[]]
        ans = []
        ans += self.combine(n-1, k)
        ans += [item + [n] for item in self.combine(n-1, k-1)]
        return ans
