class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        orglen = len(s)
        num = orglen
        if num == 0:
            return 0
        result = []
        while(num>=1):
            for i in range(0,orglen):
                if i + num  <= orglen:
                    subset = list(s[i:i + num])
                    # print 'index is', i
                    # print 'range is', num
                    # print 'subset is', subset
                    if len(set(subset)) == num:
                        return num
            num = num - 1
        return 1
