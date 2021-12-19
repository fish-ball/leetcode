class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        if not board:
            return 0
        h = ''.join(sorted(hand))
        v = {(board, h)}
        q = Deque([(board, h, 0)])
        while q:
            b, h, k = q.popleft()
            # print(b, h, k)
            hc = Counter(h)
            for x in hc:
                hc.subtract({x: 1})
                hh = ''.join(sorted(hc.elements()))
                for i in range(len(b)+1):
                    if i == len(b):
                        pass
                    elif i > 0 and b[i-1] == x:
                        continue
                    elif i > 0 and b[i]!=x and b[i-1]!=x and b[i]!=b[i-1]:
                        continue
                    # print(b,i,x, b[:i]+x+b[i:])
                    l = []
                    stk = []
                    def ap(p):
                        if not l or l[-1] != p:
                            while stk and stk[-1] >= 3:
                                del l[-stk.pop():]
                            if not l or l[-1] != p:
                                stk.append(0)
                        l.append(p)
                        stk[-1] += 1
                    for j, y in enumerate(b):
                        if i == j:
                            ap(x)
                        ap(y)
                    if i == len(b):
                        ap(x)
                    ap('')
                    bb = ''.join(l)
                    if not bb:
                        return k + 1
                    if (bb, hh) not in v:
                        v.add((bb,hh))
                        q.append((bb, hh, k+1))
                hc.subtract({x: -1})
        return -1
