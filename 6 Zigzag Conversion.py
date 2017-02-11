class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # edgecase:
        if len(s) == 0:
            return ''
        if numRows == 1:
            return s
        zigzag = {}
        for i in range(numRows):
            zigzag[i] = ''
        i, k, holder= 0, 0, 0
        updirection = True
        while(i < len(s)):
            # case0: fill 1st column
            zigzag[k] += s[i]
            if k == (numRows - 1):
                updirection = False
            elif k == 0 and not updirection:
                updirection = True
            if updirection:
                k += 1
            else:
                k -= 1
            i += 1
        output = ''
        for key in zigzag.keys():
            output += zigzag[key]

        return output
