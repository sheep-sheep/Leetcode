                
# Similar Question
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
# 
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(lo, hi):
            val = guess((lo+hi)/2)
            if val == 0:
                return (lo+hi)/2
            elif val < 0:
                return helper(lo, (lo+hi)/2-1)
            else:
                return helper((lo+hi)/2+1, hi)
        return helper(1, n)
        
# THis time i use helper to do the stack        
