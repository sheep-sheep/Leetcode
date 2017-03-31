class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lenA = len(a)
        lenB = len(b)
        res = [''] * (max(lenA, lenB) + 1)
        carry = 0
        if lenA < lenB:
            a, b = b, a
        b = '0'*(len(a)-len(b))+b
        for i in range(len(b), -1, -1):
            num = (int(a[i-1]) + int(b[i-1])) if i-1 >= 0 else 0
            if num == 2:
                res[i] = str(carry)
                carry = 1
                num = 0
            else:
                if num+carry != 2:
                    res[i] = str(num+carry)
                    carry = 0
                else:
                    res[i] = '0'
                    carry = 1
        res[0] = '' if res[0] == '0' else res[0]
        return ''.join(res)
