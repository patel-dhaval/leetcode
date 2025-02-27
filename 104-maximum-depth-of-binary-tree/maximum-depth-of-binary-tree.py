# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            
            max_lh = 1 + dfs(node.left)
            max_rh = 1 + dfs(node.right)

            depth = max(max_lh, max_rh)
            
            return depth
        
        return dfs(root)