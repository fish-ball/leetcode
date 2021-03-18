# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left >= right:
            return head
        p = None
        q = head
        if left > 1:
            p = head
            for i in range(left-2):
                p = p.next
            q = p.next
        p0 = p
        q0 = q
        for j in range(right-left+1):
            r = q.next
            q.next = p
            p = q
            q = r
        q0.next = r
        if left > 1:
            p0.next = p
            return head
        return p
