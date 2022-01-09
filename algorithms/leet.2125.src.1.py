class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a = [s.count('1') for s in bank if '1' in s]
        ans = 0
        for i in range(1, len(a)):
            ans += a[i] * a[i-1]
        return ans
