# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"

        res = []
        queue = collections.deque()

        queue.append(root)

        while queue:
            curr = queue.popleft()
            if curr:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append("N")
    
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "N":
            return None
        
        # If serialized as a string, split it back into a list
        data = data.split(",") if isinstance(data, str) else data
        root = TreeNode(int(data[0]))
        queue = collections.deque()
        queue.append(root)
        idx = 1
        while queue and (idx) < len(data):
            curr = queue.popleft()
            if data[idx] != "N":
                curr.left = TreeNode(int(data[(idx)]))
                queue.append(curr.left)
            idx+=1

            if data[idx] != "N":
                curr.right = TreeNode(int(data[idx]))
                queue.append(curr.right)
            idx+=1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))