# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        curr = root
        while True:
            if curr:
                stk.append(curr)
                curr = curr.left
            elif stk:
                curr = stk.pop()
                k -= 1
                print(curr.val)
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                break
