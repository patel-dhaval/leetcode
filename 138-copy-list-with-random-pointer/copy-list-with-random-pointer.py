"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Approach:
2 Pass approach with Hmap

First pass, create the deep copy nodes and map it against the current nodes. This pass will build the nodes

Second Pass, create the linkage, both random pointers and next pointer, on the basis of current head. Keep moving till the end of LL has reached (next pointing to null).
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {None:None}
        
        curr = head

        while curr:
            copy_node = Node(curr.val)
            old_to_new[curr] = copy_node
            curr = curr.next
        
        curr = head

        while curr:
            copy_node = old_to_new[curr]
            copy_node.next = old_to_new[curr.next]
            copy_node.random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]

