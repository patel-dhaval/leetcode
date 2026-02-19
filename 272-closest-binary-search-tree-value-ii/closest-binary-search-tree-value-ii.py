# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        deq = collections.deque()

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            deq.append(root.val)

            while len(deq) > k:
                if abs(deq[0] - target) > abs(deq[-1] - target):
                    deq.popleft()
                else:
                    deq.pop()
            
            inorder(root.right)

        inorder(root)

        return list(deq)