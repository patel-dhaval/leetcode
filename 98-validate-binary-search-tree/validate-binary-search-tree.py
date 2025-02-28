# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, node, right):
            curr = node

            if not curr:
                return True
            
            # Induction to check if val within range
            # If true, continue recursion, else return false
            # If either of the branch returns a false, terminate traversal and return False

            if left < curr.val < right:
                return dfs(left, curr.left, curr.val) and dfs(curr.val, curr.right, right)
            else:
                return False
        
        left = float("-inf")
        right = float("inf")

        return dfs(left, root, right)

            
