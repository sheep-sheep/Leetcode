# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        hi = n

        while(low+1<hi): # the break case should be the 2 numbers are adjacent,
                       # then they should differ by 1
            mid = low+(hi-low)/2
            if isBadVersion(mid):
                hi = mid
            else:
                low = mid
        
        return hi # this is not index, it's the version #
                
                
