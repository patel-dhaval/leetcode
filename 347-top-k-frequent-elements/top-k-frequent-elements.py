"""
Approach 1:
freq_arr size n+1
Sort array
for each unique element, find the count
index representing the count, append the value as a list

Parse freq_arr from desc, find values, decrement k, when k == 0, return res

TC: O(nlog n) -> sorting
SC: O(n)

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        freq_arr = [[] for _ in range(len(nums) + 1)]
        nums.sort()
        cnt = 1
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                freq_arr[cnt].append(nums[i-1])
                cnt = 1
        freq_arr[cnt].append(nums[-1])
        
        for num in freq_arr[::-1]:
            if num:
                for j in num:
                    res.append(j)
                    k-= 1
                    if k == 0:
                        return res