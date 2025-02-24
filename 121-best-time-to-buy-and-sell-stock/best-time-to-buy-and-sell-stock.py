'''
Approach
Two pointers to indicate start and end of the window, 
Goal would be to start the window at the smallest value and end the window at the highest value, thus maximizing profits

Edge cases:
return 0

L, R = 0, 1
buyP = prices[L]
maxP = 0

while R < len(prices):
    sellP= prices[R]
    if buyP > sellP:
        L = R
        buyP = prices[L]
        R = R + 1
    else:
        profit = sellP - buyP
        maxProfit = max(profit, maxProfit)
        R += 1
return maxProfit


Dry Run:

[7, 1, 5, 3]

L , R = 0, 1

buyP = 7
SellP = 1

L = 1
R = 2
buyP = 1
SellP = 5

profit = 2
maxP = 4
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        L, R = 0, 1
        buyP = prices[L]
        maxP = 0

        while R < len(prices):
            sellP = prices[R]
            if buyP > sellP:
                L = R
                buyP = prices[L]
                R += 1
            else:
                profit = sellP - buyP
                maxP = max(profit, maxP)
                R += 1
        return maxP