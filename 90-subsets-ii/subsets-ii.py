from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()  # Sort the input to handle duplicates

        def dfs(index):
            res.append(subset.copy())
            seen = set()  # Local set to track duplicates at this level

            for i in range(index, len(nums)):
                # Skip if nums[i] has already been considered at this level
                if nums[i] in seen:
                    continue
                
                seen.add(nums[i])  # Mark nums[i] as seen
                subset.append(nums[i])
                dfs(i + 1)  # Recurse to build further subsets
                subset.pop()  # Backtrack

        dfs(0)
        return res
