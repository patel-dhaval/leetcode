class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, output):
            if len(nums) == 0:
                res.append(output)
                return
            
            # Exclude the first element
            solve(nums[1:], output.copy())
            
            # Include the first element
            solve(nums[1:], output + [nums[0]])
        
        # Start the recursion with an empty list
        solve(nums, [])
        return res
