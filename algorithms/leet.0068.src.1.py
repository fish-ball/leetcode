class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        ans = []
        i = 0
        while i < n:
            j = i
            gap = maxWidth
            while j < n and gap >= len(words[j]) + j - i:
                gap -= len(words[j])
                j += 1
            buf = ''
            #print(words[i:j], gap)
            while i < j:
                buf += words[i]
                i += 1
                #print(gap, i, j)
                g = gap if j==i else 1 if j==n else -int(-gap//(j-i))
                if g:
                    buf += ' ' * g
                gap -= g
            ans.append(buf)
        return ans
