class TrieNode:
    def __init__(self, c, end = False, nxt = None):
        self.c = c
        self.end = end
        self.nxt = nxt or {}

    @classmethod
    def build(cls, word, node=None):
        # print('build', word, node)
        c = word[0]
        if node and c in node.nxt:
            nd = node.nxt[c]
        else:
            nd = cls(c)
            if node:
                node.nxt[c] = nd
        if len(word) == 1:
            nd.end = True
        else:
            cls.build(word[1:], nd)
        return node or nd

    def disp(self, prefix=''):
        # print(prefix+('$' if self.end else ''))
        for k, v in self.nxt.items():
            v.disp(prefix+k)
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode('')
        for w in words:
            TrieNode.build(w, trie)
        # trie.disp()
        n = len(board)
        m = len(board[0])
        b = [[False] * m for i in range(n)]
        ans = set()

        def dfs(x, y, nd: TrieNode, path=''):
            # print(x, y, nd, path)
            b[x][y] = True
            if nd.end:
                # print('!!BINGO!!', path)
                ans.add(path)
            for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
                xx = x + dx
                yy = y + dy
                if 0<=xx<n and 0<=yy<m and not b[xx][yy] and board[xx][yy] in nd.nxt:
                    cc = board[xx][yy]
                    dfs(xx, yy, nd.nxt[cc], path+cc)
            b[x][y] = False

        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if c in trie.nxt:
                    dfs(i, j, trie.nxt[c], c)
        return sorted(ans)
