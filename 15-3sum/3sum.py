class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        res = []
        while target < len(nums):
            if nums[target] > 0:
                break
            
            L, R = target + 1, len(nums) - 1

            while L < R:
                if nums[target] + nums[L] + nums[R] == 0:
                    res.append([nums[target], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1                
                    while nums[R] == nums[R + 1] and L < R:
                        R -= 1
                elif nums[target] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
            target += 1
            while  target < len(nums) and nums[target] == nums[target - 1]:
                target += 1
        
        return res