# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(0, head)
        last = root
        while last.next:
            p = last.next
            q = p.next
            if not q:
                break
            r = q.next
            last.next = q
            last.next.next = p
            last.next.next.next = r
            last = last.next.next
        return root.next
