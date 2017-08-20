class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1*1
        if n==3:
            return 1*2
        product = 1
        while(n>4):
            product *= 3
            n -= 3
        product *= n
        return product
        
# 1. use the f = x(N-x) to get the max point of break should be N/2*N/2
# 2. whenever there's a new N, we can treat to break it down to the min
# 3. which gives us 2 bases, 2 and 3
# 4. since 3*3 > 2*2*2, we should use 3 as the factor and break them into 3 as many as possible

# then the question will be transformed to how do you break the number to get 3s.
