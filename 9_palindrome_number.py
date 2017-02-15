class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x%10 == 0):
            return False

        num = 0
        while(x > num):
            num = num*10 + x%10
            x = x/10
        return x == num or x == num/10
