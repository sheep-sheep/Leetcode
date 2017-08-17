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

# max profit means the last sell - first buy, the difference is max.
# and we need a variable to record the minmum buy value, and since the buy and sell is in order,
# if we go from left to right, we can always find the last sell and first buy difference.

# Then we use current price minus first buy min, then we will have max profit at current position.

# This doesn't feel like a DP, oh, yes, it is, becasue i use the variable to reduce the complexity!
