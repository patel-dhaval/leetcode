class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        pred_stack = []
        succ_stack = []
        
        # --- Helper Functions (Your Code!) ---
        def init_preds(node):
            while node:
                if node.val <= target:
                    pred_stack.append(node)
                    node = node.right
                else:
                    node = node.left
                    
        def init_succs(node):
            while node:
                if node.val >= target:
                    succ_stack.append(node)
                    node = node.left
                else:
                    node = node.right
                    
        def get_next_pred():
            node = pred_stack.pop()
            val = node.val
            node = node.left
            while node:
                pred_stack.append(node)
                node = node.right
            return val
            
        def get_next_succ():
            node = succ_stack.pop()
            val = node.val
            node = node.right
            while node:
                succ_stack.append(node)
                node = node.left
            return val
            
        # --- Main Logic ---
        
        # 1. Initialize both stacks
        init_preds(root)
        init_succs(root)
        
        # 2. Handle the "Duplicate Target" case
        # If target exists, both stacks have it. Move one forward to avoid double counting.
        if pred_stack and succ_stack and pred_stack[-1].val == succ_stack[-1].val:
            get_next_pred() # Burn one instance
            
        res = []
        
        # 3. Merge Loop: Find k closest
        while k > 0:
            if not pred_stack:
                res.append(get_next_succ())
            elif not succ_stack:
                res.append(get_next_pred())
            else:
                # Compare distances
                pred_val = pred_stack[-1].val
                succ_val = succ_stack[-1].val
                
                if abs(target - pred_val) < abs(target - succ_val):
                    res.append(get_next_pred())
                else:
                    res.append(get_next_succ())
            k -= 1
            
        return res