class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        # the key info here is you have to choose the adjacent numbers between each row.
        # and we have to calculate the path for each idx, which will conver the question to
        # a matrix like problem.

        dp = [[0] * len(nums) for nums in triangle]

        for (i, nums) in enumerate(triangle):
            for (j, num) in enumerate(nums):
                if i == 0 and j == 0:
                    dp[i][j] = triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == (len(nums) - 1):
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[-1])
