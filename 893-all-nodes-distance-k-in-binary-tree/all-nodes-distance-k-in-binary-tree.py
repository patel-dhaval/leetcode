# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentNodes = {}

        def getParent(node, parent):
            if not node:
                return

            parentNodes[node] = parent

            getParent(node.left, node)
            getParent(node.right, node)

        visited = set()
        distance = k
        res = []

        def dfs(node, distance):
            if not node or node in visited or distance < 0:
                return None

            visited.add(node)
            
            if distance == 0:
                res.append(node.val)

            dfs(node.left, distance-1)
            dfs(node.right, distance-1)
            dfs(parentNodes[node], distance - 1)


        getParent(root, None)
        dfs(target, k)

        return res