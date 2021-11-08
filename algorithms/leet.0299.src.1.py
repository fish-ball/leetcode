class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = sum([1 if x == y else 0 for x, y in zip(secret, guess)])
        b = sum((Counter(secret) & Counter(guess)).values()) - a
        return f'{a}A{b}B'
