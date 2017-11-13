3. my own DP
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
2. reduce memory
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit_max =0 
        buy_min = float('inf')
        for (pos, price) in enumerate(prices):
                buy_min = min(buy_min, price)
                profit_max = max(profit_max, price-buy_min)
        return profit_max

1. Standard DP    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # initialize
        n = len(prices) + 1
        dp = [[0] * n for _ in range(n)]

        # base case:dp[0][0] is 0
        for i in range(1, n):
            for j in range(1, n):
                if i < j:  # this is the valid buy&sell case
                    dp[i][j] = max(dp[i][j - 1], prices[j-1] - prices[i-1])
        return max([profit[-1] for profit in dp])
    

# 2nd is the right way to do, i was so bad at that time
