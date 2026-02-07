class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        deq = collections.deque()
        
        def inorder(node):
            if not node: 
                return
            
            inorder(node.left)
                        
            if len(deq) == k:
                # Check if the current node is "worse" than the furthest node in our window (deq[0])
                if abs(target - node.val) < abs(target - deq[0]):
                    # Current node is BETTER. Remove the "loser" (furthest away) and add the winner.
                    deq.popleft()
                    deq.append(node.val)
                else:
                    # Current node is WORSE.
                    # Since the tree is sorted, every node after this will be EVEN WORSE.
                    return 
            else:
                deq.append(node.val)
                
            inorder(node.right)
        
        inorder(root)
        return list(deq)