class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        totalMoves = m-1 + n-1
        import math
        def nCr(total,r):
            f = math.factorial
            return f(total)/f(r)/f(total-r)
        return nCr(totalMoves, min([m,n])-1)

    
# Fundemantal DP Solution:
# 1. suppose the number of paths to arrive at a point (i, j) 
#    is denoted as P[i][j], it is easily concluded that P[i][j] = P[i - 1][j] + P[i][j - 1].
# 2. These conditions can be handled by initialization (pre-processing) --- 
#    initialize P[0][j] = 1, P[i][0] = 1 for all valid i, j.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        aux = [[1 for x in range(n)] for x in range(m)]
        # initialize the DP table
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
