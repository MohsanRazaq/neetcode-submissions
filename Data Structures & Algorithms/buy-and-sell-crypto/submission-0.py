class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price,max_profit=prices[0],0

        for curr_price in prices:
            min_price=min(curr_price,min_price)
            today_profit=curr_price-min_price
            max_profit=max(today_profit,max_profit)

        return max_profit
        
        #Time complexity, O(n), only one linear iteration
        # spcae complexity, O(1)