class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def isPalindrom(s):
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def getSubStrings(s):
            if len(s) == 0:
                return [[]]
            if len(s) == 1:
                return [[s]]
            res = []
            for i in range(len(s)):
                if isPalindrom(s[:i+1]):
                    for sub_string in getSubStrings(s[i+1:]):
                        res.append([s[:i+1]] + sub_string)
            return res

        return getSubStrings(s)


print Solution().partition('bb')
