class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return Counter(magazine) - Counter(ransomNote) + Counter(ransomNote) == Counter(magazine)
