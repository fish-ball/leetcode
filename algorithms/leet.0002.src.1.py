# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = ListNode()
        p = root
        while l1 or l2:
            x = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            l1 = l1 and l1.next 
            l2 = l2 and l2.next
            carry = x // 10
            p.next = ListNode(x % 10)
            p = p.next
        if carry:
            p.next = ListNode(1)
        return root.next
