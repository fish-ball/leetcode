# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            if p.next and p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
