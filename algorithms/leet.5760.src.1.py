class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        mis1a = sum([1 if c == '0' else 0 for c in s[::2]])
        mis1b = sum([1 if c == '1' else 0 for c in s[1::2]])
        mis2a = sum([0 if c == '0' else 1 for c in s[::2]])
        mis2b = sum([0 if c == '1' else 1 for c in s[1::2]])
        print(mis1a, mis1b, mis2a, mis2b)
        kk = []
        if mis1a == mis1b:
            kk.append(mis1a)
        if mis2a == mis2b:
            kk.append(mis2a)
        return min(kk) if kk else -1
