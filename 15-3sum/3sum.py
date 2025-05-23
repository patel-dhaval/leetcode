class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
        
            while l < r:
                target = nums[i] + nums[l] + nums[r]

                if target > 0:
                    r-=1
                elif target < 0:
                    l+=1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        
        return res
                