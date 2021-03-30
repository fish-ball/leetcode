# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        k = k % n
        if not k:
            return head

        p = head
        for i in range(k):
            p = p.next
        q = head
        x = p
        y = q
        while p:
            t = p
            y = q
            q = q.next
            p = p.next
        t.next = head
        y.next = None
        return q
