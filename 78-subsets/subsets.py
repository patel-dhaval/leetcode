class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generateSubsets(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            generateSubsets(i+1, subset)
            subset.pop()
            generateSubsets(i+1, subset)

        generateSubsets(0, [])

        return res