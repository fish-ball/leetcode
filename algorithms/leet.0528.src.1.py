class Solution:

    def __init__(self, w: List[int]):
        s = sum(w)
        n = len(w)
        self.w = [x / s for x in w]
        for i in range(1, n):
            self.w[i] += self.w[i-1]


    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.random())



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
