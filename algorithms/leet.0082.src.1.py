# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = ListNode(0, head)
        p = h
        while p.next and p.next.next:
            # print(p.val)
            if p.next.val != p.next.next.val:
                p = p.next
                continue
            while p.next.next and p.next.val == p.next.next.val:
                p.next.next = p.next.next.next
            p.next = p.next.next
        return h.next
                
