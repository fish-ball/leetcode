# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s = []
        p = head
        while p:
            s.append(p.val)
            p = p.next
        return max([x+y for x, y in zip(s, s[::-1])])
