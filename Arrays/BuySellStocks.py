'''
LC 121. Best Time to Buy and Sell Stock
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] > prices[l]:
                max_profit = max(max_profit, prices[i] - prices[l])
            else:
                l = i
                
        return max_profit