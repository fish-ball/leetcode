class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(None)
        def dfs(*qty):
            if sum(qty) == 0:
                return 0
            ans = sum(k*price[i] for i, k in enumerate(qty))
            for i, row in enumerate(special):
                row2 = list(qty)
                for j, x in enumerate(row[:-1]):
                    row2[j] -= x
                if min(row2) < 0:
                    continue
                ans = min(ans, row[-1] + dfs(*row2))
            return ans
        return dfs(*needs)
