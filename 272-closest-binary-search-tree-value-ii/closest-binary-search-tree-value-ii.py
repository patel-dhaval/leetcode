# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root, target, k):
        deq = collections.deque()

        def inorder(node):
            if not node: return
            inorder(node.left)

            # Sliding Window Logic
            deq.append(node.val)
            if len(deq) > k:
                # If the new element is closer than the oldest (leftmost), remove the oldest
                if abs(target - deq[0]) > abs(target - deq[-1]):
                    deq.popleft()
                else:
                    # If the new element is WORSE than the oldest, we are moving away!
                    # Since it's sorted, we can stop early (Pruning optimization).
                    deq.pop()
                    return 

            inorder(node.right)

        inorder(root)
        return list(deq)