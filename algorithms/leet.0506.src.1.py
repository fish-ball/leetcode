class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        for i, s in enumerate(sorted(score, reverse=True)):
            d[s] = {
                0: 'Gold Medal',
                1: 'Silver Medal',
                2: 'Bronze Medal'
            }.get(i, str(i+1))
        return [d[s] for s in score]
        
