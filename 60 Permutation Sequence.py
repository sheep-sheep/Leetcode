class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        elements = range(1, n+1)
        NN = reduce(operator.mul, elements) # n!
        k, result = (k-1) % NN, ''
        while len(elements) > 0:
            NN = NN / len(elements)
            i, k = k / NN, k % NN
            result += str(elements.pop(i))
        return result
