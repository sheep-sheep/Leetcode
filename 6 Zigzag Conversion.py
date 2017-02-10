class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ''
        if numRows == 1:
            return s
        zigzag = {}
        for i in range(numRows):
            zigzag[i] = ''
        i, k, holder= 0, 0, 0
        while(i < len(s)):
            if i!=0 and (i-holder)%numRows == 0:
                if numRows !=2:
                    zigzag[numRows/2] += s[i]
                    holder += 1
                    i += 1
                k = 0
                if i == len(s):
                    break
            # case0: fill 1st column
            zigzag[k] += s[i]
            i += 1
            k += 1
        output = ''
        for key in zigzag.keys():
            output += zigzag[key]

        return output
