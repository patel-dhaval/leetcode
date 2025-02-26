"""

Clarifying questions

Edge cases

Approach
So the idea is to find the rate, k, at which koko eats bananas from the pile
this k has to be minimum so that koko can complete eating all the bananas within the specified h hours

Here, brute force would be to check the rates from k = max value within the pile, till 0 to find the minimum k
But that would be O(n) computation, as for each value of k, we will process the pile.

This can be done better by using binary search.
We can assume that the lowest rate would fall within the lowest and the largest pile value
I.E: if we try to search for values within that range and compare with h, we will know which half of the range is likely to have the optimal value of h

This would lower the TC from O(n) to o(log n)

Code

Dry run

TC and SC

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_k = float("inf")
    
        while low <= high:
            mid = (low + high) // 2
            calc_h = 0
            for i in piles:
                calc_h += ceil(i/mid)
            if calc_h <= h:
                min_k = min(mid, min_k)
                high = mid -1
            else:
                low = mid + 1
        return min_k