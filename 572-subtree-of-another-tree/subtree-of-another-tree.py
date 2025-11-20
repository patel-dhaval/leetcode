# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2) -> bool:
            if not node1 and not node2:
                return True

            if (not node1 or not node2):
                return False
            if node1.val != node2.val:
                return False
            if node1 and node2 and node1.val == node2.val:
                left = dfs(node1.left, node2.left)
                right = dfs(node1.right, node2.right)
                return left and right
        
        if not subRoot:
            return True 
        if not root:
            return False
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and dfs(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
