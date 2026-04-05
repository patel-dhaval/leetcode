# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heights = collections.defaultdict(list)
        res = []
        def dfs(node):
            nonlocal heights
            if not node:
                return 0
            
            lh = dfs(node.left)
            rh = dfs(node.right)
            height = max(lh, rh)

            heights[height].append(node.val)

            return 1 + height
        
        dfs(root)
        for k, v in heights.items():
            res.append(v)
        
        return res