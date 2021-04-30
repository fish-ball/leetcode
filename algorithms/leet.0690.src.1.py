"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = dict([(e.id, e) for e in employees])
        s = [d[id]]
        ans = 0
        while s:
            e = s.pop()
            ans += e.importance
            for i in e.subordinates:
                s.append(d[i])
        return ans
