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
        def find_root(node):
            if node.parent == None:
                return node
            
            return find_root(node.parent)
        
        root = find_root(p)
        
        def LCA(node):
            curr = node
            
            if not curr:
                return None

            if curr == p or curr == q:
                return node
            
            left = LCA(curr.left)
            right = LCA(curr.right)
            
            if left and right:
                return curr
            elif left:
                return left
            else:
                return right
        
        return LCA(root)