class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        p = self.d
        for c in word:
            p[c] = p.get(c, {})
            p = p[c]
        p['end'] = True
        # print(self.d)

    def search(self, word: str) -> bool:
        q = [self.d]
        for c in word:
            q2 = []
            for p in q:
                if c == '.':
                    q2 += [p[k] for k in p if k != 'end']
                elif c in p:
                    q2.append(p[c])
            q = q2
        # print(q)
        for d in q:
            # print(d, d.keys())
            if 'end' in d.keys():
                return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
