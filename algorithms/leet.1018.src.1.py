class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        x = 0
        ans = []
        for y in A:
            x *= 2
            x += y
            x %= 5
            ans.append(x == 0)
        return ans
            
