class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        calcK = 0
        minK = max(piles)
        while low <= high:
            calcK = 0
            mid = (low + high)//2
            for i in piles:
                calcK += math.ceil(float(i)/mid)
            if calcK <= h:
                minK = min(mid, minK)
                high = mid - 1
            elif calcK > h:
                low = mid + 1
        
        return minK