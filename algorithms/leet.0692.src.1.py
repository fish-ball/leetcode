class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        idx = {}
        stk = []
        for w in words:
            if w not in idx:
                idx[w] = len(stk)
                stk.append([w, 0])
            m = idx[w]
            stk[m][1] += 1
            while m > 0 and (stk[m][1] > stk[m-1][1] or 
                    stk[m][1] == stk[m-1][1] and stk[m][0] < stk[m-1][0]):
                stk[m], stk[m-1] = stk[m-1], stk[m]
                idx[stk[m][0]] = m
                idx[stk[m-1][0]] = m - 1
                m -= 1
        # print(stk)
        return [stk[i][0] for i in range(k)]
