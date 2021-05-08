class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort()
        n = len(jobs)
        w = [0] * k
        ans = sum(jobs)
        d = dict()
        def dfs(i):
            nonlocal ans
            # print(f'dfs({i})', w)
            key = f'{i}:{sorted(w)}'
            if i >= n:
                ans = max(w)
                # print(f'  >> !! {ans}')
                return ans
            if key in d:
                return d[key]
            best = ans
            for v, j in sorted(zip(w, range(k))):
                if w[j] + jobs[i] < ans:
                    w[j] += jobs[i]
                    better = dfs(i + 1)
                    if better < best:
                        best = better
                    w[j] -= jobs[i]
            d[key] = best
            return best
        return dfs(0)
        
