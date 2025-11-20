# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def dfs(node):
            nonlocal max_dia
            if not node:
                return 0
            
            max_lh = dfs(node.left)
            max_rh = dfs(node.right)

            depth = max(max_lh, max_rh)
            dia = max_lh + max_rh
            max_dia = max(max_dia, dia)
            
            return 1 + depth
        
        dfs(root)

        return max_dia