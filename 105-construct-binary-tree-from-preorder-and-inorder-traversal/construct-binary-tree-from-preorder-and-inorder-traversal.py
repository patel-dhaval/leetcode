# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        pivot = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:pivot+1],inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        return root
    