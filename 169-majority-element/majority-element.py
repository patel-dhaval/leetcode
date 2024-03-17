class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            major_elem = 0
            count = 0
    
            for i in range(0, len(nums)):
                    
                if count == 0:
                    major_elem = nums[i]

                if nums[i] == major_elem:
                    count += 1
                else:
                    count -= 1
                    
            return major_elem