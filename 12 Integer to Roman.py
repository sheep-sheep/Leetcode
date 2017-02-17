class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # The special rule of Roman Numeral is there's no char repeating 4 times
        # which will be represented with subtraction.
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        #    0,   1,   2,    3,     4,    5,    6,    7,     8,      9

        return (M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10])
