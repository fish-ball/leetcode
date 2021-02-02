class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        nxt = [-1] * n
        first = [-1] * 26
        last = [-1] * 26
        cnt = [0] * 26
        ans = 0
        for i, c in enumerate(s):
            o = ord(c) - ord('A')
            if last[o] != -1:
                nxt[last[o]] = i
            else:
                first[o] = i
            last[o] = i
            cnt[o] += 1
            while i - first[o] + 1 - cnt[o] > k and nxt[first[o]] > -1:
                first[o] = nxt[first[o]]
                cnt[o] -= 1
            ans = max(ans, min(n, cnt[o]+k))
        return ans
            

