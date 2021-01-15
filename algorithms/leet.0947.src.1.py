class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        p = [-1] * n
        dx = dict()
        dy = dict()

        def find(k):
            if p[k] == -1:
                return k
            p[k] = find(p[k])
            return p[k]

        for i, (x, y) in enumerate(stones):
            if x in dx:
                p[i] = find(dx[x])
            else:
                dx[x] = i
            if y in dy:
                p[i] = find(dy[y])
            else:
                dy[y] = i
            xx = find(dx[x])
            yy = find(dy[y])
            if xx != yy:
                p[xx] = yy

        print(p)
        
        return n - len(set([find(i) for i in range(n)]))
