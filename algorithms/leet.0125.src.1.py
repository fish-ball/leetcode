class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c.lower() for c in s if c.isalnum()]
        for i in range(len(a) // 2):
            if a[i] != a[-1-i]:
                return False
        return True
