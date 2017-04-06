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

# Right anwser:
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        right = x
        left = 1
        if x == 0 or x == 1:
            return x
        while(True):
            mid = left + (right - left)/2
            if mid*mid>x:
                right =mid - 1
            elif (mid+1)*(mid+1) > x: # Tricky part is here, the return type is Int, we don't need to calculate it to double
                                      # mid+1 to verify mid is the only Choice
                return mid            # Another issue here is x*x will have potential to become overflow, we better use x/mid
            else:
                left = mid + 1
