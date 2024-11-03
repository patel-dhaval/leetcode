# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs_height(root):
            if root == None:
                return 0

            lh = dfs_height(root.left)
            rh = dfs_height(root.right)

            return 1 + max(lh, rh)
        
        return dfs_height(root)