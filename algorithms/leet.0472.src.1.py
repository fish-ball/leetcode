class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        # 建 Trie
        root = {'#': 0, '&': ''}
        nodes = [root]
        for w in words:
            p = root
            for c in w:
                if c not in p:
                    p[c] = {'#': len(nodes), '&': c}
                    nodes.append(p[c])
                p = p[c]
            p['$'] = True
        # 枚举检索
        for w in words:
            q = {(0, 0)}
            for c in w:
                qq = set()
                for i, d in q:
                    p = nodes[i]
                    if c not in p:
                        continue
                    p = p[c]
                    qq.add((p['#'], d))
                    if p.get('$'):
                        qq.add((0, min(d+1, 2)))
                q = qq
            if any((1 for i, d in q if i == 0 and d >= 2)):
               ans.append(w)
        return ans
