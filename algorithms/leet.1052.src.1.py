class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        b = sum(a for a, b in zip(customers, grumpy) if not b)
        for i, a in enumerate(customers):
            customers[i] = a * grumpy[i]
        acc = sum(customers[:X])
        ans = acc
        for i in range(X, N):
            acc += customers[i]
            acc -= customers[i-X]
            ans = max(ans, acc)
        ans += b
        return ans
