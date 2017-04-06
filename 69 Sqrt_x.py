# Newton method
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """    
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

    
# Binary Search
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        right = x
        left = 1
        while(True):
            mid = left + (right - left)/2
            if mid*mid>x:
                right =mid - 1
            elif mid*mid == x:
                return mid
            else:
                left = mid + 1
