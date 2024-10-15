# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxi = 0

        def dfs_height(root):
            nonlocal maxi
            if root == None:
                return 0

            lh = dfs_height(root.left)
            rh = dfs_height(root.right)

            maxi = max(maxi, lh + rh)
            return 1 + max(lh, rh)
        
        dfs_height(root)

        return maxi