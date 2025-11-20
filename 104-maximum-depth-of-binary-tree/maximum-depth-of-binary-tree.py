# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> int:
            if not root:
                return 0
            
            max_l = dfs(root.left)
            max_r = dfs(root.right)

            max_h = max(max_l, max_r)

            return 1 + max_h
        
        return dfs(root)