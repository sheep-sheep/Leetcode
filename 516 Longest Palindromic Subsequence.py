class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [[1 if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]
        for i in range(N+1, 0, -1):
            # The reason it needs backwards is dp[i+1] is requiring the next position's result.
            # if we go from bottom, all the values will be unknown.
            for j in range(i+1, N+1):
                if i < j:
                    dp[i][j] = dp[i+1][j-1] + 2 if (s[i - 1] == s[j - 1]) else max(dp[i+1][j], dp[i][j-1])
        return dp[1][N]
