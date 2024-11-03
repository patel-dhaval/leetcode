# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque()
        res = []
        queue.append(root)
        
        while queue:
            len_q = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(i, len(queue))
                if i == len_q - 1:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return res