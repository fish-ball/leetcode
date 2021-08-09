# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = 0
        n2 = 0
        p1 = headA
        p2 = headB
        while p1:
            n1 += 1
            p1 = p1.next
        while p2:
            n2 += 1
            p2 = p2.next
        p1 = headA
        p2 = headB
        if n1 > n2:
            n1, n2 = n2, n1
            p1, p2 = p2, p1
        for i in range(n1, n2):
            p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                break
            p1 = p1.next
            p2 = p2.next
        return p1
