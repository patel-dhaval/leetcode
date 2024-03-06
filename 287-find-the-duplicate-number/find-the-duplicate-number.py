class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] +=1
            else:
                count[i] = 1

        for k,v in count.items():
            if v > 1:
                return k
        