# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total_good_nodes = 0
        def dfs(node, max_val) -> None:
            if not node:
                return

            nonlocal total_good_nodes

            if node.val >= max_val:
                total_good_nodes += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        
        dfs(root, root.val)

        return total_good_nodes