class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        def dfs(begin, end):
            # print(f'dfs({begin}, {end})')
            nonlocal ans
            if end - begin <= ans:
                return
            mp = [0] * 26
            for i in range(begin, end):
                mp[ord(s[i])-ord('a')] += 1
            last = begin
            ok = True
            for i in range(begin, end):
                if mp[ord(s[i])-ord('a')] < k:
                    ok = False
                    dfs(last, i)
                    last = i + 1
            if ok:
                ans = end - begin
                # print(f'ans = {ans}')
            else:
                dfs(last, end)
        dfs(0, len(s))
        return ans
