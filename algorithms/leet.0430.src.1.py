"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stk = []
        p = head
        while p:
            if p.child:
                if p.next:
                    stk.append(p.next)
                q = p.child
                p.child = None
                p.next, q.prev = q, p
            if not p.next and stk:
                q = stk.pop()
                p.next, q.prev = q, p
            p = p.next

        return head
