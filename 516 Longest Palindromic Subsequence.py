class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [[1 if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]

        for i in range(0, N):
            for j in range(i, N+1):
                if i != j:
                    dp[i][j] = dp[i+1][j-1] + 2 if (s[i - 1] == s[j - 1]) else max(dp[i-1][j], dp[i][j+1])
        return dp[N][1]

print Solution().longestPalindromeSubseq("bbbab")
