class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        
        nums.sort(reverse=True)
        target = sum_nums // k

        if nums[0] > target: 
            return False
            
        used = [False] * len(nums)
        
        def backtrack(idx, k, subsetSum):
            
            if k == 0:
                return True

            if subsetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(idx, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue

                if j > idx and nums[j] == nums[j-1] and not used[j-1]:
                    continue
                
                used[j] = True

                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True

                used[j] = False

                if subsetSum == 0:
                    return False

            return False

        return backtrack(0, k, 0)
