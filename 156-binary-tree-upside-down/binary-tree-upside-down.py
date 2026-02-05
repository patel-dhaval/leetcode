# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        curr = root
        stack = []

        while curr:
            stack.append(curr)
            curr = curr.left
        
        new_root = stack.pop()
        while stack:
            node = stack.pop()
            node.left.left = node.right
            node.left.right = node
            node.left, node.right = None, None

        return new_root