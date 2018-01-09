class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        # the 3rd inner loop to check each position and find max profit is unnecessary
        # we can try to use a tmp variable to reduce the time complexity
        k = 2
        dp = [[0] * (len(prices) + 1) for _ in range(k + 1)] # this means the max profit with k transctions.
        for i in range(1, k+1):
            # initial
            tmpMaxProfit = dp[i - 1][0] - prices[0] # use this varaible to get the profit at each transctions
            for j in range(1, len(prices)+1):
                # dp[i][j]  1> dp[k][j-1]
                #           2> for m in range(j-1]:
                #                   prices[j] + dp[k-1][m]- prices[m]
                
                # Trick is, the prev buy choice could be any price before j-1, thus you have to check or find the max local
                # and that would be your new value, then use tmpMaxProfit
                # tmpMaxProfit = dp[i-1][j-1] - prices[j-1]: use one variable to reduce the loop
                dp[i][j] = max(dp[i][j - 1],  tmpMaxProfit + prices[j-1])
                tmpMaxProfit = max(tmpMaxProfit, dp[i - 1][j-1] - prices[j-1])
        return dp[-1][-1]
