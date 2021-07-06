class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        t = {}
        f = set()
        for name, table, food in orders:
            table = int(table)
            tb = t[table] = t.get(table, {})
            f.add(food)
            tb[food] = tb.get(food, 0) + 1
        ans = [['Table'] + sorted(f)]
        f = sorted(f)
        for tbk in sorted(t.keys()):
            ans.append([str(tbk)] + [str(t[tbk].get(food, 0)) for food in f])
        return ans

