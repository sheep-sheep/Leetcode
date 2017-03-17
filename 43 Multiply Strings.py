class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        size1 = len(num1)
        size2 = len(num2)
        result = [0]*(size1+size2)
        count1 = size1 - 1
        count2 = size2 - 1
        for i in num1[::-1]:
            for j in num2[::-1]:
                mul = (ord(i) - ord('0'))*(ord(j) - ord('0'))
                pos1 = count1 + count2
                pos2 = count1 + count2 + 1
                sumofnums = mul + result[pos2]

                result[pos1] += sumofnums/10
                result[pos2] = sumofnums%10
                count2 -= 1
            count1 -= 1
        final = ''
        for c in result:
            final += chr(ord('0')+c)
        return final
