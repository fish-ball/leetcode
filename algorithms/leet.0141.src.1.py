# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p = head
        q = head
        while True:
            q = q.next and q.next.next
            p = p.next
            if not q:
                return False
            if p == q:
                return True
