# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []

        def dfs(node, sum):
            if not node:
                return False
            
            stack.append(node)

            sum += node.val

            if not node.left and not node.right:
                if targetSum == sum:
                    return True

            if dfs(node.left, sum):
                return True
            if dfs(node.right, sum):
                return True

            stack.pop()

            return False

        return dfs(root, 0)




