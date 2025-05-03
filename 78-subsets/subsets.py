class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def subsets(index, currSet, res):
            if index >= len(nums):
                res.append(currSet.copy())
                return
        
            currSet.append(nums[index])
            subsets(index+1, currSet, res)
            currSet.pop()
            subsets(index+1, currSet, res)

            return res
        
        return subsets(0, [], [])

        
        



            