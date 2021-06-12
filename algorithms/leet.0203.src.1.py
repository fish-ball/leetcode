# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = ListNode(next=head)
        p = root
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return root.next
