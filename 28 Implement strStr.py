class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        length = len(needle)
        count = 0
        for i in haystack:
            if count + length - 1 < len(haystack):
                if haystack[count: count + length] == needle:
                    return count
            else:
                return -1
            count += 1
        return -1
