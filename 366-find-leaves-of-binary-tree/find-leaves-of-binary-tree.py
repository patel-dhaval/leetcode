# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BruteForce
        """
        # res = []
        # def dfs(node):
            
        #     if not node:
        #         return
        #     if not node.left and not node.right:
        #         res[-1].append(node.val)
        #         return True
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)
            
        #     if left:
        #         node.left = None
        #     if right:
        #         node.right = None
        
        
        # while root.left or root.right:
        #     res.append([])
        #     dfs(root)
        
        # res.append([root.val])
        # return res
        
        output = collections.defaultdict(list)
    
        def dfs(node, height):
            if not node: 
                return height 
            left = dfs(node.left, height)
            right = dfs(node.right, height)
            height = max(left, right)
            output[height].append(node.val)
            return height + 1
        
        dfs(root, 0)
        return list(output.values())
