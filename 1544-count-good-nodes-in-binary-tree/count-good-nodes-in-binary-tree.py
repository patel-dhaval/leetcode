# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count_good_nodes = 0
        def dfs(node, maxi):
            nonlocal count_good_nodes
            curr = node
            if not curr:
                return
            
            if curr.val >= maxi:
                maxi = curr.val
                count_good_nodes +=1
            
            dfs(curr.left, maxi)
            dfs(curr.right, maxi)

            return
        
        dfs(root,float("-inf"))
        return count_good_nodes
