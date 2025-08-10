class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) < 2:
            return 0
        
        L, R = 0, 1

        while R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                max_profit = max(max_profit, prices[R] - prices[L])
            R+=1
            
        return max_profit