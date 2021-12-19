class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = Counter([c.lower() for c in licensePlate if c.isalpha()])
        #print(lp)
        ans = None
        for w in words:
            if ans and len(ans) <= len(w):
                continue
            #print(list((Counter(w)-lp).elements()))
            if len(list((Counter(w)-lp).elements())) == len(w)-len(list(lp.elements())):
                ans = w
        return ans
