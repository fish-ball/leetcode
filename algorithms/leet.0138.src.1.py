"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p = head
        while p:
            p.next = Node(p.val, next=p.next)
            p = p.next.next
        h2 = head.next
        p = head
        while p:
            p.next.random = p.random and p.random.next
            p = p.next.next
        p = head
        while p:
            q = p.next
            pn = p.next.next
            qn = pn and pn.next
            p.next, q.next = pn, qn
            p = pn
        return h2
