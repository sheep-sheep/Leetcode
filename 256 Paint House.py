GREEN = 0
RED = 1
BLUE = 2
class Solutions(object):
    def minCost(self, n):
        dp = [[0 for _ in 3] for _ in n]
        dp[i][RED] = min(dp[i - 1][GREEN], dp[i - 1][BLUE]) + cost[i - 1][RED]
        dp[i][BLUE] = min(dp[i - 1][RED], dp[i - 1][GREEN]) + cost[i - 1][BLUE]
        dp[i][GREEN] = min(dp[i - 1][RED], dp[i - 1][BLUE]) + cost[i - 1][GREEN]
