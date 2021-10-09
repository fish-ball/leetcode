class SummaryRanges:

    def __init__(self):
        self.next = [-1] * 10001
        self.heads = set()

    def addNum(self, val: int) -> None:
        # print(f'addNum: {val}')
        if self.next[val] != -1:
            return
        if val > 0 and self.next[val-1] != -1:
            self.next[val - 1] = val
        else:
            self.heads.add(val)
        if val < 10000  and self.next[val+1] != -1:
            self.next[val] = val + 1
            self.heads.remove(val+1)
        else:
            self.next[val] = val
        # print(self.heads)
        # print(self.next[:10])

    def getIntervals(self) -> List[List[int]]:
        def last(i):
            if self.next[i] == i:
                return i
            self.next[i] = last(self.next[i])
            return self.next[i]
        return [[i, last(i)] for i in sorted(self.heads)]




# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
