class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        
        target = sum_nums // k

        if nums[0] > target: 
            return False
            
        bucket_sums = [0] * k
        
        # 3. Recursion: Try to put 'nums[index]' into one of the k buckets
        def backtrack(index):
            # Base Case: We placed all numbers successfully!
            if index == len(nums):
                return True
                
            num = nums[index]
            
            # Try every bucket
            for i in range(k):
                # Check if it fits
                if bucket_sums[i] + num <= target:
                    bucket_sums[i] += num
                    
                    # If this placement leads to a solution, return True
                    if backtrack(index + 1): 
                        return True
                    
                    # Backtrack: Remove it and try the next bucket
                    bucket_sums[i] -= num
                    
                    # Optimization: If this bucket is empty and we couldn't 
                    # make it work, putting 'num' in the next empty bucket 
                    # is the same thing. Stop to save time.
                    if bucket_sums[i] == 0:
                        break
                        
            return False

        return backtrack(0)
