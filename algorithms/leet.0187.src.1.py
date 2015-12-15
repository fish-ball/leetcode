class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = dict()
        for i in range(len(s)):
            t = s[i:i+10]
            d[t] = d.get(t, 0) + 1
        return [k for k in d if d[k] > 1]
                
                
            
