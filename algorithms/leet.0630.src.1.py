class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        cs = sorted(((b, a) for a, b in courses))
        # print(cs)
        dp = [0]
        for b, a in cs:
            for i in range(len(dp),0,-1):
                if dp[i-1] > b-a:
                    continue
                if i >= len(dp):
                    dp.append(dp[i-1]+a)
                elif dp[i] > dp[i-1]+a:
                    dp[i] = dp[i-1]+a
            # print(dp)
        return len(dp)-1
