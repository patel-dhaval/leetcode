class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = nums
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for num in arr:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        for i in range(cnt0):
            arr[i] = 0

        for i in range(cnt0, cnt0 + cnt1):
            arr[i] = 1

        for i in range(cnt0 + cnt1, len(arr)):
            arr[i] = 2
