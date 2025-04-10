class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        max_subarrays = 0
        l = 0
        temp_sum = 0
        temp_avg = 0
        target_sum = k * threshold
        for r in range(len(arr)):
            temp_sum += arr[r]
            if (r - l +1) == k:
                # temp_avg = temp_sum//(r-l+1)
                if temp_sum >= target_sum:
                    max_subarrays += 1
                temp_sum -= arr[l]
                l += 1

        return max_subarrays