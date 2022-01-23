class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i, (p, b) in enumerate(questions):
            dp[i+1] = max(dp[i], dp[i+1])
            dp[min(n, i+b+1)] = max(dp[min(n, i+b+1)], dp[i]+p)
            # print(dp)
        return dp[-1]
            
