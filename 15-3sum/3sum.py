class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i in range(len(nums)):
            if nums[i] > 0 or i > len(nums) - 2:
                break
            target = nums[i]
            j = i + 1 
            k = len(nums) - 1

            while j < k:
                if target + nums[j] + nums[k] > 0:
                    k -= 1
                elif target + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                    while nums[k] == nums[k+1] and j < k:
                        k-=1
            i += 1
            while i in range(len(nums)) and nums[i] == nums[i-1]:
                i += 1
                
        return res
