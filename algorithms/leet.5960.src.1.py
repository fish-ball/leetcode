class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([w[:1].upper()+w[1:].lower() if len(w) > 2 else w.lower() for w in title.split()])
