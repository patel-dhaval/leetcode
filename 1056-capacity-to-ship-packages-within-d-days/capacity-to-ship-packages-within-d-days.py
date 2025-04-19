class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_capacity = sum(weights)
        low = max(weights)
        high = max_capacity

        while low <= high:
            mid = (low + high)//2
            sum_w = 0
            day_t = 1
            for w in weights:
                if sum_w + w > mid:
                    day_t += 1
                    sum_w = 0
                sum_w += w
            if day_t > days:
                low = mid + 1
            else:
                high = mid - 1
                max_capacity = min(max_capacity, mid)
        
        return max_capacity