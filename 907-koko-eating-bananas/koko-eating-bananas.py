class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        We will use binary search to identify the minimum rate
        Rate would lie between 1 and the max value of bananas in a pile
        We will compute rates and compare the resultant h
        Keep continuing till calc_h is lower than h

        TC: O(log n)
        SC: O(1)
        """

        # min_bananas = 1
        # max_bananas = max(piles)

        # while min_bananas < max_bananas:
        #     mid = (min_bananas + max_bananas)//2

        #     calc_h = 0

        #     for pile in piles:
        #         calc_h += ceil(pile/mid)
            
        #     if calc_h > h:
        #         min_bananas = mid + 1
        #     else:
        #         max_bananas = mid

        # return min_bananas

        """
        Uses binary search to find the minimum bananas/hour Koko needs to eat.
        
        Search Space: [1, max(piles)]
        For each speed, calculate total hours needed and adjust bounds accordingly.

        Time Complexity: O(n log(max(piles)))
        Space Complexity: O(1)
        """
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2  # Overflow-safe style
            hours = sum(ceil(pile / mid) for pile in piles)

            if hours > h:
                left = mid + 1  # Too slow
            else:
                right = mid  # Could be slower

        return left