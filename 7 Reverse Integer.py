class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = abs(x)
            negative = True
        num = str(x)
        num = num[::-1]
        if int(num) > 2**31:
            return 0
        output = 0 - int(num) if negative else int(num)
        return output
