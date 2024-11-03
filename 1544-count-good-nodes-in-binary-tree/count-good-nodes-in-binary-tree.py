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
            if not root:
                return 0
            
            result = 0

            if root.val >= max_path_val:
                max_path_val = root.val
                result +=1
            
            result += dfs(root.left, max_path_val)
            result += dfs(root.right, max_path_val)
            print("res", result)
            return result

        return dfs(root, max_path_val)