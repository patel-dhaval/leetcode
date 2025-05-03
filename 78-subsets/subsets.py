class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def subsets(index, currSet, res):
            
            if index > len(nums):
                return

            res.append(currSet.copy())
            
            for i in range(index, len(nums)):
                currSet.append(nums[i])
                subsets(i+1, currSet, res)
                currSet.pop()
            
            return res
        
        return subsets(0, [], [])

        
        



            