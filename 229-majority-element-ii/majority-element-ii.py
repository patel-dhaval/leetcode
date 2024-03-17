class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = {}
        soln = []

        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] +=1
            
        for k,v in hmap.items():
            if v > len(nums)/3:
                soln.append(k)
        
        return soln