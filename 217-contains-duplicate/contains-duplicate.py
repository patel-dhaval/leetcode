"""
Approach: Reduce the number of look-ups to see if duplicate elements are present
Thus, using a set would be better as the lookup in a set is o(1) operation, for n operations, overall it would remain as o(n)
Thus, utilize a set for the lookup operations, and if an element found in the set, mark return false and end processing
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        viewed_elements = set()

        for n in nums:
            if n not in viewed_elements:
                viewed_elements.add(n)
            else:
                return True
        
        return False