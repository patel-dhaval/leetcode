class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # low, high = 1, max(piles)
        # calcK = 0
        # minK = max(piles)
        # while low <= high:
        #     calcK = 0
        #     mid = (low + high)//2
        #     for i in piles:
        #         calcK += math.ceil(float(i)/mid)
        #     if calcK <= h:
        #         minK = min(mid, minK)
        #         high = mid - 1
        #     elif calcK > h:
        #         low = mid + 1
        
        # return minK
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res