class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = 0
        sell = 1
        profit = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                # We found a lower price to buy stock. Update buying index
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        
        return profit