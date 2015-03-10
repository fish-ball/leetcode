class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = dict()
        for i in range(len(num)):
            d[num[i]] = i + 1
        for a in d:
            if target - a > a and target - a in d:
                return list(sorted((d[a], d[target - a])))
        ans = []
        for i in range(len(num)):
            if num[i] + num[i] == target:
                ans.append(i + 1)
        return tuple(ans)
