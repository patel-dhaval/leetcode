# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, k):
            stack = []
            curr = node
            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    print(curr.val)
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
            

                    
        return dfs(root, k)
            


