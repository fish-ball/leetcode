# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(next)
        p = head
        q = h
        last = h
        while p:
            if p.val == 0:
                q.next = ListNode()
                last = q
                q = q.next
            else:
                q.val += p.val
            p = p.next
        last.next = None
        return h.next
