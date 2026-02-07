# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff_stack = []

        stack = []
        curr = root
        # stack.append(curr)
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                diff = abs(target - curr.val)
                if not diff_stack:
                    diff_stack.append([diff, curr.val])
                elif diff_stack[-1][0] > diff:
                    diff_stack.append([diff, curr.val])
                curr = curr.right
            
        return diff_stack[-1][1]

        