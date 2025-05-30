class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if goal <= i + nums[i]:
                goal = i
        
        if goal == 0 :
            return True
        
        return False
