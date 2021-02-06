class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        acc = sum(cardPoints[:n-k])
        ans = acc
        for i in range(n-k, n):
            acc += cardPoints[i] - cardPoints[i-n+k]
            ans = min(ans, acc)
        return sum(cardPoints) - ans

