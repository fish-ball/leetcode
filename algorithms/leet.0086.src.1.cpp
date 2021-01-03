# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        a = ListNode(0)
        pa = a
        b = ListNode(1)
        pb = b
        while head:
            if head.val < x:
                pa.next = head
                pa = pa.next
            else:
                pb.next = head
                pb = pb.next
            head = head.next
        pa.next = b.next
        return a.next
