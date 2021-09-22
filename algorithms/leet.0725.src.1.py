# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        ans = []
        while n:
            m = -(-n//k)
            ans.append(head)
            p = head
            for i in range(m-1):
                p = p.next
            head = p.next
            p.next = None
            n -= m
            k -= 1
        return ans + [None] * k
            
