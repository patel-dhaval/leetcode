class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        while fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break

        slow2 = nums[0]

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow