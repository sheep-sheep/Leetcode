class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        dp = [((0,1), 0)]+[((i,i+1), heights[i-1]) for i in range(1, len(heights))]

        for i in range(1, len(heights)+1):
            newhist = (dp[i-1][0][1]+1-dp[i-1][0][0])*min(dp[i-1][1], heights[i-1])
            oldhist = (dp[i-1][0][1]-dp[i-1][0][0])*dp[i-1][1]
            hist = heights[i-1]

            if newhist>=hist:
                if newhist>oldhist:
                    dp[i] = ((dp[i][0][1]+1-dp[i][0][0]), min(dp[i-1][1], heights[i-1]))
                else:
                    dp[i] = (dp[i - 1][0], dp[i - 1][1])
            elif newhist<oldhist:
                dp[i] = (dp[i-1][0], dp[i-1][1])
            else:
                dp[i] = (1, heights[i-1])
        return max(dp[-1][0]*dp[-1][1], tmp[0]*tmp[1])
