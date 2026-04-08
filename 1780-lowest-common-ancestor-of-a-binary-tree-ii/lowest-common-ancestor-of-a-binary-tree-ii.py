# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.found_p = False
        self.found_q = False

        node = self.dfs(root, p, q)

        if self.found_p and self.found_q:
            return node
        
        return None

    def dfs(self, node, p, q):
        if not node:
            return False
        
        left = self.dfs(node.left, p,q)
        right = self.dfs(node.right, p, q)

        if node.val == p.val:
            self.found_p = True
            return node

        if node.val == q.val:
            self.found_q = True
            return node
        
        if left and right:
            return node
        
        return left if left else right


# # N-ary Tree variation for this 

# class Solution:
#     def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
#         self.found_p = False
#         self.found_q = False

#         node = self.dfs(root, p, q)

#         if self.found_p and self.found_q:
#             return node
        
#         return None

#     def dfs(self, node, p, q):
#         if not node:
#             return None
        
#         # 1. Post-order: Traverse ALL children completely before doing anything else
#         found_in_children = []
#         for child in node.children:
#             res = self.dfs(child, p, q)
#             if res:
#                 found_in_children.append(res)
        
#         # 2. Process current node: Update flags
#         if node.val == p.val:
#             self.found_p = True
#         if node.val == q.val:
#             self.found_q = True
        
#         # 3. If two different child branches returned targets, this is the LCA
#         if len(found_in_children) == 2:
#             return node
            
#         # 4. If the current node itself is p or q, bubble it up to the parent
#         if node.val == p.val or node.val == q.val:
#             return node
            
#         # 5. Otherwise, bubble up whatever was found in the children (if anything)
#         return found_in_children[0] if found_in_children else None
