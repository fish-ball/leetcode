class MapSum:

    def __init__(self):
        self.d = {'val': 0}

    def insert(self, key: str, val: int) -> None:
        def proc(d, k):
            if k >= len(key):
                other = sum(d[x].get('val') for x in d.keys() if x != 'val')
                cur = d.get('val', 0) - other
                d['val'] = other + val
                return val - cur
            if key[k] not in d:
                d[key[k]] = {'val': 0}
            inc = proc(d[key[k]], k+1)
            d['val'] += inc
            return inc
        proc(self.d, 0)

    def sum(self, prefix: str) -> int:
        d = self.d
        for c in prefix:
            if c not in d:
                return 0
            d = d[c]
        return d['val']

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
