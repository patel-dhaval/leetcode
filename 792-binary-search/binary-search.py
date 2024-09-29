class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(arr, x, low, high):
            if low > high:
                return -1
            
            mid = (low + high)//2

            if x == arr[mid]:
                return mid
            elif x > arr[mid]:
                return binarySearch(arr, x, mid + 1, high)
            else:
                return binarySearch(arr, x, low, mid - 1)

        if(len(nums)) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        low, high = 0, len(nums)-1

        return binarySearch(nums, target, low, high)
