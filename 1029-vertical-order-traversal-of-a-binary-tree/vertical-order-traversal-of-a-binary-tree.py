# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
    
        temp = deque([(root, 0, 0)])
        
        while temp:
            node, x, y = temp.popleft()
            
            nodes[x].append((y, node.val))
            
            if node.left:
                temp.append((node.left, x - 1, y + 1))
            if node.right:
                temp.append((node.right, x + 1, y + 1))
        result = []
        
        for x in sorted(nodes.keys()):
            column = sorted(nodes[x], key=lambda p: (p[0], p[1]))
            result.append([val for y, val in column])
        
        return result 
