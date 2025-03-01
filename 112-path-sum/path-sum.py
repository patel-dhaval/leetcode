# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, pathSum, targetSum):
            
            if not node:
                return False

            curr = node

            pathSum = pathSum + curr.val
            
            if (not curr.left and not curr.right):
                if targetSum == pathSum:
                    return True
                else:
                    pathSum = pathSum - curr.val
                    return False
            
            return dfs(curr.left, pathSum, targetSum) or dfs(curr.right, pathSum, targetSum)
        
        return dfs(root, 0, targetSum)