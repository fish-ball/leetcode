class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d = list(Counter(nums).items())
        n = len(d)
        path = Counter()
        # print(d)

        def dfs(k, x):
            if k == 0 and x == 0 or x > 0:
                yield list(path.elements())
            # print(f'dfs({k}, {x})')
            if k < n:
                if x < d[k][1]:
                    path.subtract({d[k][0]: -1})
                    yield from dfs(k, x+1)
                    path.subtract({d[k][0]: 1})
                yield from dfs(k+1, 0)

        return list(dfs(0, 0))
