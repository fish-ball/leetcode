class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        kk = dict()

        for a, b in envelopes:
            if a not in kk:
                kk[a] = set()
            kk[a].add(b)
        
        stk = [0]
        last = 0

        for a, bb in sorted(kk.items()):
            for i in range(len(stk)-1, -1, -1):
                for b in sorted(bb):
                    if b > stk[i]:
                        if i == len(stk) - 1:
                            stk.append(b)
                        else:
                            stk[i+1] = min(stk[i+1], b)
                        break
        
        return len(stk) - 1
