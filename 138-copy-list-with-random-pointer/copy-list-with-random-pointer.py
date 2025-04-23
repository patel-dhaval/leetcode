"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {None:None}
        
        curr = head
        while curr:
            newNode = Node(curr.val)
            old_to_new[curr] = newNode
            curr = curr.next

        curr = head

        while curr:
            newNode = old_to_new[curr]
            if curr.next:
                newNode.next = old_to_new[curr.next]
            if curr.random:
                newNode.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
