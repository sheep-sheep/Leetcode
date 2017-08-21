class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # when think up the DP solution, DP will stand for True/False instead of number of palindrome.
        # It's because when you set it to #, it's very hard to build the relationship between N and N-1.
        if len(s) == 0:
            return 0
        N = len(s)
        dp = [[1 if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]
        count = 0
        for i in range(1, N+1):
            for j in range(i, 0, -1):
                # since we need next pos's info to decide current info, we can't use ascending order, we need
                # descending order
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 if (s[i - 1] == s[j - 1]) and (dp[i - 1][j + 1] or j+1==i) else 0 # The special case to consider 'AA'
                if dp[i][j]:
                    count += 1
        return count
