class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        N = len(pairs)
        if N == 0:
            return 0
        pairs.sort()
        dp = [0]*(N+1)
        dp[1] = 1
        pair = pairs[0]
        for i in range(2, N+1):
            if pairs[i-1][0]>pair[1]:
                dp[i] = dp[i-1] + 1
                pair = pairs[i-1]
            else:
                dp[i] = dp[i-1]
            
        return dp[-1]
            
