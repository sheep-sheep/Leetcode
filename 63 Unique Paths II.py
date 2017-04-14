class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        aux = [[0 for x in range(n+1)] for x in range(m+1)]
        aux[0][1] = 1
        # initialize the DP table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
