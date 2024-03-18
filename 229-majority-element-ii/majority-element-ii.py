class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums) # size of the array

        cnt1, cnt2 = 0, 0 # counts
        el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

        # applying the Extended Boyer Moore’s Voting Algorithm:
        for i in range(n):
            if cnt1 == 0 and el2 != nums[i]:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i]:
                cnt2 = 1
                el2 = nums[i]
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ls = [] # list of answers

        # Manually check if the stored elements in
        # el1 and el2 are the majority elements:
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1

        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)

        return ls


        # Hmap Solution - Non optimal
        # hmap = {}
        # soln = []

        # for i in nums:
        #     if i not in hmap:
        #         hmap[i] = 1
        #     else:
        #         hmap[i] +=1
            
        # for k,v in hmap.items():
        #     if v > len(nums)/3:
        #         soln.append(k)
        
        # return soln