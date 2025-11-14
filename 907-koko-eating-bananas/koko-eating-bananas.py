class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_rate = max(piles)
        while low < high:
            mid = (low + high)//2
            hours = 0
            for p in piles:
                hours += ceil(p/mid)

            if hours > h:
                low = mid +1
            else:
                high = mid
                min_rate = min(high, min_rate)
        return min_rate