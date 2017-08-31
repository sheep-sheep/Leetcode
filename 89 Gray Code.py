class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def convertNum(bits):
            N = len(bits)
            res = 0
            for bit in bits:
                res += 2^(N-1)*bit
                N -= 1
            return res
        
        res = [0]*n
        for i in range(1, n+1):
            res[i] = res[i-1]*2+1
