class Solution:
    def compute_nearest_smallest_left(self, ns_left, ip):
        val_stack = []
        for idx, val in enumerate(ip):
            if not val_stack:
                ns_left.append(-1)        
            elif val_stack and val_stack[-1][0] < ip[idx]:
                ns_left.append(val_stack[-1][1])
            elif val_stack and val_stack[-1][0] >= ip[idx]:
                while val_stack and val_stack[-1][0] >= ip[idx]:
                    val_stack.pop()
                if not val_stack:
                    ns_left.append(-1)
                else:
                    ns_left.append(val_stack[-1][1])
            val_stack.append([ip[idx], idx])
        return ns_left

    
    def compute_nearest_smallest_right(self, ns_right, ip):
        val_stack = []
        for idx in range(len(ip)-1, -1, -1):
            if not val_stack:
                ns_right.append(len(ip))
            elif val_stack and val_stack[-1][0] < ip[idx]:
                ns_right.append(val_stack[-1][1])
            elif val_stack and val_stack[-1][0] >= ip[idx]:
                while val_stack and val_stack[-1][0] >= ip[idx]:
                    val_stack.pop()
                if not val_stack:
                    ns_right.append(len(ip))
                else:
                    ns_right.append(val_stack[-1][1])
            val_stack.append([ip[idx], idx])
        return ns_right[::-1]

    def largestRectangleArea(self, heights: List[int]) -> int:
        ns_left = []
        ns_right = []

        res = [0 for _ in range(len(heights))]
        left = self.compute_nearest_smallest_left(ns_left, heights)
        right = self.compute_nearest_smallest_right(ns_right, heights)

        for idx,val in enumerate(heights):
            res[idx] = val * (right[idx] - left[idx] - 1)
        return max(res)

