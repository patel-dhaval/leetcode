class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        soln_arr = set()

        for n in nums:
            if n in soln_arr:
                return True
            soln_arr.add(n)
        
        return False