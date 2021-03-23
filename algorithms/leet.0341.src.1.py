# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def iterate(ls):
            for x in ls:
                if x.isInteger():
                    # print(x.getInteger())
                    yield x.getInteger()
                else:
                    yield from iterate(x.getList())

        self.fn = iterate(nestedList)
        try:
            self.buf = next(self.fn)
        except:
            self.buf = None

    def next(self) -> int:
        ans = self.buf
        try:
            self.buf = next(self.fn)
        except:
            self.buf = None
        return ans
    
    def hasNext(self) -> bool:
        return self.buf is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
