class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res_arr = [0 for _ in range(len(temperatures))]
        val_stack = []

        for idx, temp in enumerate(temperatures):
            while val_stack and val_stack[-1][1] < temp:
                res_arr[val_stack[-1][0]] = idx - val_stack[-1][0]
                val_stack.pop()
            val_stack.append([idx, temp])
        
        return res_arr
