# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            max_lh = dfs(node.left)
            max_rh = dfs(node.right)

            if max_lh == -1 or max_rh == -1:
                return -1
            
            if abs(max_lh - max_rh) > 1:
                return -1

            depth = max(max_lh, max_rh)
            
            return 1 + depth
        
        if dfs(root) == -1:
            return False
        return True