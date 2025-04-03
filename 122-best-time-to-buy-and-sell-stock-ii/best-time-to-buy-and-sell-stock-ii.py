class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currently_holding = False
        profit = 0
        total_profit = 0
        curr_pp = 0

        for i in range(len(prices)):
            if i < len(prices) - 1:
                if prices[i] <= prices[i+1] and not currently_holding:
                    curr_pp = prices[i]
                    currently_holding = True
                    # print(curr_pp)
                elif (prices[i] > prices[i+1] and currently_holding):
                    profit = prices[i] - curr_pp
                    # print("profit", profit)
                    currently_holding = False
                    curr_pp = 0
                    total_profit += profit
            elif currently_holding and i == len(prices)-1:
                profit = prices[i] - curr_pp
                currently_holding = False
                curr_pp = 0
                total_profit += profit
        return total_profit
