class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dd = {}
        for (i, x) in enumerate(nums2):
            if x not in dd:
                dd[x] = []
            dd[x].append(i)
        stk = [-1]
        for x in nums1:
            if x not in dd:
                continue
            target = dd[x]
            m = len(target)
            for i in range(len(stk), 0, -1):
                y = stk[i-1]
                # 这里改成二分会更快
                for j, z in enumerate(target):
                    if z > stk[i-1]:
                        if i == len(stk):
                            stk.append(z)
                        else:
                            stk[i] = min(stk[i], z)
                        break
            # print(stk)
        return len(stk) - 1



