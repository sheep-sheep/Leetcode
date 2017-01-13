class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = {}
        longest, i, j = 0, 0, 0
        for j in range(len(s)):
            if s[j] not in sub.keys():
                sub[s[j]] = j
                longest = max(longest, len(sub.keys()))
            else:
                i = sub[s[j]] + 1
                sub = {}
                for num in range(i, j+1): # range is [)
                    sub[s[num]] = num
            j += 1
        return longest
    
# def lengthOfLongestSubstring(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     orglen = len(s)
#     num = orglen
#     if num == 0:
#         return 0
#     result = []
#     while (num >= 1):
#         for i in range(0, orglen):
#             if i + num <= orglen:
#                 subset = list(s[i:i + num])
#                 # print 'index is', i
#                 # print 'range is', num
#                 # print 'subset is', subset
#                 if len(set(subset)) == num:
#                     return num
#         num = num - 1
#     return 1
