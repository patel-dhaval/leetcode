# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        max_path_val = float("-inf")

        def dfs(root, max_path_val):
            nonlocal result
            if not root:
                return 0
            
            if root.val >= max_path_val:
                result += 1
            max_path_val = max(max_path_val, root.val)

            dfs(root.left, max_path_val)
            dfs(root.right, max_path_val)

            return result

        return dfs(root, max_path_val)