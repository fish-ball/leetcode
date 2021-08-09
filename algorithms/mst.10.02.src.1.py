class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        a = []
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in d:
                d[ss] = []
                a.append(d[ss])
            d[ss].append(s)
        return a
