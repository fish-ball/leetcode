class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return s.strip() and len(s.strip().split(' ')[-1]) or 0
