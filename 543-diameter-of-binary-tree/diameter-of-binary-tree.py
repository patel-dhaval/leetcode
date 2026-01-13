# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 0
        
        def dfs(root):
            nonlocal max_depth
            if not root:
                return 0
            
            max_l = dfs(root.left)
            max_r = dfs(root.right)

            max_depth = max(max_depth, (max_l + max_r))

            return 1 + max(max_l, max_r)

        dfs(root)

        return max_depth
