# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = collections.deque()

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            queue.append(node.val)

            if len(queue) > k:
                if abs(queue[0] - target) > abs(queue[-1]- target):
                    queue.popleft()
                else:
                    queue.pop()
                    return
            
            inorder(node.right)
        
        inorder(root)

        return list(queue)
            
