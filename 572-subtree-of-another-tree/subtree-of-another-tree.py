# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def isSameTree(node1, node2) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        if not subRoot:
            return True 
        if not root:
            return False

        stack = [root]

        while stack:
            curr = stack.pop()
            if not curr:
                continue

            if curr.val == subRoot.val:
                if isSameTree(curr, subRoot):
                    return True
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False
