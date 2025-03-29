"""
Approach:
Use a hashmap of the number and index
check for target - num, if its in map, If present in map, return the index of both the numbers
If not found, add the current number and its index to the map
Since its given solution does exists, by the end of the input processing, we will find the result
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed_numbers = {}

        for i in range(len(nums)):
            potential_pair_number = (target - nums[i])
            if potential_pair_number in viewed_numbers.keys():
                return [viewed_numbers[potential_pair_number], i]
            else:
                viewed_numbers[nums[i]] = i