"""
Need to find: Min weight capacity of ship to ship in days mentioned
Total Weight of the input needs to be loaded in days mentioned

ip: [1,2,3,4,5]
days: 2
find: min weight of ship to ship all in 2 days and shipments in order.

ip: [1,2,3,4,5]
days: 2

low: 1, 9, 9, 9, 9
high: 15, 15, 11, 9, 8
mid: 8, 12, 10, 9
temp_sum: 1 + 2 + 3, 4, 5, 1 + 2 + 3 + 4, 5, 1 + 2 + 3 + 4, 5, 1 + 2 + 3, 4 + 5
temp_days: 2
lowest_capacity: 15, 12, 10, 9

"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = sum(weights)
        low = max(weights)
        high = total_weight
        lowest_capacity = total_weight

        while low < high:
            mid = (low + high)//2
            temp_days = 1
            temp_sum = 0
            i = 0
            for weight in weights:
                if temp_sum + weight > mid:
                    temp_days += 1
                    temp_sum = 0
                temp_sum += weight
            if temp_days <= days:
                lowest_capacity = min(lowest_capacity, mid)
                high = mid
            else:
                low = mid + 1
        
        return lowest_capacity
