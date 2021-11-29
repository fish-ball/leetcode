class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        x = random.randrange(0, self.rem)
        self.rem -= 1
        idx = self.h.get(x, x)
        self.h[x] = self.h.get(self.rem, self.rem)
        return [idx//self.n, idx%self.n]

    def reset(self) -> None:
        self.rem = self.m * self.n
        self.h = {}

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
