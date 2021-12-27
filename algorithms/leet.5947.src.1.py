class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rr = dict(zip(recipes, ingredients))
        
        # print()
        # print(supplies)
        # for r, q in rr.items():
        #     print(f'{r}: {q}')
        ss = set(supplies)
        ans = []
        p = set()
        @lru_cache(None)
        def yes(x):
            nonlocal p
            p.add(x)
            if x in ss:
                p.remove(x)
                return True
            if x in rr:
                for i in rr[x]:
                    if i in p:
                        p.remove(x)
                        return False
                    if not yes(i):
                        p.remove(x)
                        return False
                p.remove(x)
                return True
            p.remove(x)
            return False
        for r in recipes:
            p = set()
            # print(r, rr.get(r,[]), r in ss, yes(r))
            if yes(r):
                ans.append(r)
        return ans
