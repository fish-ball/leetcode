class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ww = {}
        ws = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask = mask | (1<<ord(c)-ord('a'))
            ww[mask] = ww.get(mask, 0) + 1
            ws[mask] = w
        # print('abcdefghijklmnopqrstuvwxyz')
        # for b, c in ww.items():
            # print(bin((1<<26)+b)[-26:][::-1], c, ws[b])
        ans = []
        print('---')
        for p in puzzles:
            a = [1<<ord(c)-ord('a') for c in p]
            acc = 0
            for b in range(1<<6):
                mask = a[0] + sum(a[i+1] for i in range(6) if (1<<i)&b)
                # if ww.get(mask):
                    # print(bin((1<<26)+mask)[-26:][::-1], ww.get(mask, 0), ws[mask])
                acc += ww.get(mask, 0)
            ans.append(acc)
        return ans
