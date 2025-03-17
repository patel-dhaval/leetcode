"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while p is not None or q is not None:
            if p is not None:
                if p.val in visited:
                    return p
                visited.add(p.val)
                p = p.parent

            if q is not None:
                if q.val in visited:
                    return q
                visited.add(q.val)
                q = q.parent