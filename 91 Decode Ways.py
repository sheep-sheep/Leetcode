class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        dp = [1] * len(s)
        if len(s)==1:
            if s[0]=='0':
                return 0
            else:
                return 1
        for i in range(1, len(s) + 1):
            if s[i-1] == '0':
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i - 1] if int(s[i - 1:i + 1]) > 26 else dp[i - 1] + dp[i - 2]
        return dp[-1]
