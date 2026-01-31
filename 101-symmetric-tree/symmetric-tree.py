# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkTree(node1, node2):            
            
            if (not node1 and not node2):
                return True

            if (node1 and not node2) or (node2 and not node1) or node1.val != node2.val:
                return False
            
            if node1.val == node2.val:
                left = checkTree(node1.left, node2.right)
                right = checkTree(node1.right, node2.left)
                if left and right:
                    return True
                return False

        if not root:
            return True

        return checkTree(root.left, root.right)