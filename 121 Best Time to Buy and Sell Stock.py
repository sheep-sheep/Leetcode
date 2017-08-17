class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        dp = [0]*len(prices)
        buy_min = 0
        for (pos, price) in enumerate(prices):
            if pos == 0:
                dp[pos] = 0
                buy_min = price
            else:
                buy_min = price if price <=buy_min else buy_min
                dp[pos] = max(dp[pos-1], price-buy_min)

        return dp[-1]
