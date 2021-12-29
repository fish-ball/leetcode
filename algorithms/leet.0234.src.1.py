# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        p = head
        while p:
            a.append(p.val)
            p = p.next
        return a == a[::-1]
