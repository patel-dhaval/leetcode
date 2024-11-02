# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(root, val):
        
            if not root:
                return None
            
            if val > root.val:
                return self.searchBST(root.right, val)
            elif val < root.val:
                return self.searchBST(root.left, val)
            else:
                return root

        sub_tree_root = search(root, val)

        if sub_tree_root == None:
            return None
        
        return sub_tree_root