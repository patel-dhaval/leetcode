# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        first_min = root.val
        second_min = float('inf')
        found_min = False
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr.val > first_min:
                second_min = min(second_min, curr.val)
                found_min = True
                continue
            else:
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        
        return second_min if found_min else -1

            


