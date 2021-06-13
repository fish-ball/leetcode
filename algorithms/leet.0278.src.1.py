# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n+1
        while l+1<r:
            m = l+r+1>>1
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r
