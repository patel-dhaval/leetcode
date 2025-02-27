# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        soln = []
        if root:
            queue.append(root)
        
        while queue:
            curr_queue_len = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i == curr_queue_len - 1:
                    soln.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return soln