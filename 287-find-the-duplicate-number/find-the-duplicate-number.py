class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
        # # Linear space solution, not optimal
        # count = {}
        # for i in nums:
        #     if i in count.keys():
        #         count[i] +=1
        #     else:
        #         count[i] = 1

        # for k,v in count.items():
        #     if v > 1:
        #         return k
        