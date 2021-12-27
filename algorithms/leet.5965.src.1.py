class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        d = {}
        n = len(arr)
        ans = [-1] * n
        for i, x in enumerate(arr):
            if x not in d:
                d[x] = []
            d[x].append(i)
            
        for v, ii in d.items():
            k = len(ii)
            dd = sum(ii)
            p = 0
            # print(v, ii)
            for j, i in enumerate(ii):
                # 左边有i个，右边有k-i个
                dp = i - p
                dd -= (k-j)*dp
                dd += j*dp
                
                ans[i] = dd
                p = i
        return ans
                
