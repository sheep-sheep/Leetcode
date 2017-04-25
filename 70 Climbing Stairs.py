class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

# Using DP is faster and trade of Space, make use of the sub solution
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            a = [1]*(n+1)
            for i in range(2, n+1):
                a[i] = a[i-2] + a[i-1]
            return a[n]
