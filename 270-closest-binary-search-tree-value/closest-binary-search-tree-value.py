# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val
        stack = [root]
        
        while stack:
            node = stack.pop()            
            if abs(target - node.val) < abs(target - closest):
                closest = node.val
            elif abs(target - node.val) == abs(target - closest):
                closest = min(closest, node.val)
                
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            
        return closest


        # # Good for BT but need to optimize for BST
        # diff_stack = []
        # stack = []
        # curr = root
        # while stack or curr:
        #     if curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     else:
        #         curr = stack.pop()
        #         diff = abs(target - curr.val)
        #         if not diff_stack:
        #             diff_stack.append([diff, curr.val])
        #         elif diff_stack[-1][0] > diff:
        #             diff_stack.append([diff, curr.val])
        #         curr = curr.right
            
        # return diff_stack[-1][1]

        