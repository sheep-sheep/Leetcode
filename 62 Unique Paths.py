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
