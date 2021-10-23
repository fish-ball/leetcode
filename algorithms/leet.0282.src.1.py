class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)
        def dfs(i, p):
            # print(f'dfs({i}, {p})')
            if i == n:
                if eval(p) == target:
                    ans.append(p)
                return
            j = len(p)-1
            while j > 0 and p[j] == '0':
                j -= 1
            is_zero = p[j] in '+*-0'
            # print(p, is_zero, j, p[j])
            for o in ('+-*' if is_zero else ['','+','-','*']):
                dfs(i+1, p+o+num[i])
        dfs(1, num[0])
        return ans
