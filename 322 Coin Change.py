class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

    
# We note that this problem has an optimal substructure property, which is the key piece 
# in solving any Dynamic Programming problems. In other words, the optimal solution can 
# be constructed from optimal solutions of its subproblems.     

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = float('inf')
        dp = [0]+[inf]*amount
        for i in range(1, amount+1):
            dp[i] = min(dp[i-coin]+1 if (i-coin)>=0 else inf for coin in coins)
        return dp[-1] if dp[amount]!=inf else -1
