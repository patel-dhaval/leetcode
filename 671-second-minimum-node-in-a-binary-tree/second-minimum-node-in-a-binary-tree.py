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
            
        # The global minimum is always at the root
        min_val = root.val
        
        # Initialize second_min to infinity so we can minimize it later
        second_min = float('inf')
        found_second = False
        
        # Standard BFS Queue
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Case 1: We found a value larger than the root (Candidate found)
            if node.val > min_val:
                # Update the answer if this is the smallest "second min" seen so far
                second_min = min(second_min, node.val)
                found_second = True
                # STOP traversing this branch. Children are guaranteed to be >= node.val
                continue 
            
            # Case 2: node.val == min_val (Keep searching)
            # If the value is the same as root, the second min might be deeper in this branch
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return second_min if found_second else -1
