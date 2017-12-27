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


# Previous solution was so bad

        class Solution(object):
            def lengthOfLongestSubstring(self, s):
                s = list(s)
                helper = {}
                begin = 0
                end = 0
                count = 0
                maxLen = 0
                while end < len(s):
                    if s[end] not in helper:
                        helper[s[end]] = 1
                    else:
                        helper[s[end]] += 1
                        count += 1
                    end += 1
                    
                    while count > 0:
                        if helper[s[begin]] > 1:
                            count -= 1
                        helper[s[begin]] -= 1
                        if helper[s[begin]] == 0:
                            del helper[s[begin]]
                        begin += 1
                    maxLen = max(maxLen, end - begin)
                return maxLen  
