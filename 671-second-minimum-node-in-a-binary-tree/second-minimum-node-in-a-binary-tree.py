# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        min_val = root.val
        second_min = float('inf')
        found_second = False
        
        while queue:
            curr = queue.popleft()
            if curr.val > min_val:
                second_min = min(curr.val, second_min)
                found_second = True
                continue
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return second_min if found_second else -1
            
