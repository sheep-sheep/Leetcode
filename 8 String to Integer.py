class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # remove the leading spaces and the spaces in the middle
        str = str.strip(' ')

        # deal with the positive and negative sign
        signed = False
        if str.startswith('-'):
            signed = True
            str = str[1:]
        elif str.startswith('+'):
            signed = False
            str = str[1:]
        else:
            signed = False

        num = 0
        # check the invalid symbols & INTMAX
        for char in str:
            if char <= '9' and char >='0':
                num = num*10 + int(char)
                if signed and num >= 1<<31:
                    num = 1<<31
                    break
                elif not signed and num >= (1<<31) - 1:
                    num = (1<<31) - 1
                    break
            else:
                break
        if signed:
            num = -num
        return num
    
class Solution_1(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # remove the leading spaces and the spaces in the middle
        str = str.strip(' ')
        str = str.replace(' ', '')

        # deal with the positive and negative sign
        signed = False
        if str.startswith('-'):
            signed = True
            str = str.replace('-', '')
        elif str.startswith('+'):
            signed = False
            str = str.replace('+', '')
        else:
            signed = False

        num = 0
        # check the invalid symbols & INTMAX
        for char in str:
            if char <= '9' and char >='0':
                num = num*10 + int(char)
                if signed and num >= 1<<31:
                    num = 1<<31
                    break
                elif not signed and num >= 1<<31 - 1:
                    num = (1<<31) - 1
                    break
            else:
                break
        if signed:
            num = -num
        return num
