class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles)
        res_rate = max_rate
        while min_rate < max_rate:
            mid_rate = (min_rate + max_rate)//2
            temp_hours = 0
            for p in piles:
                temp_hours = temp_hours + ceil(p/mid_rate)
            
            if temp_hours > h:
                min_rate = mid_rate + 1
            else:
                res_rate = min(res_rate, mid_rate)
                max_rate = mid_rate
        
        return max_rate
                