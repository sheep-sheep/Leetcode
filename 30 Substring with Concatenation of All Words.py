class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def _findSubstring(left, right, stringlength, wordlength, totallength, s, map, result):
            curr = {}
            while right + wordlength <= stringlength:
                word = s[right: right + wordlength]
                right += wordlength
                if word not in map.keys():
                    left = right
                    curr = {}
                else:
                    curr[word] = curr[word] + 1 if word in curr.keys() else 1
                    while curr[word] > map[word]:
                        curr[s[left: left+wordlength]] -= 1
                        left += wordlength
                    if right - left == totallength:
                        result.append(left)

        # Edge Cases are checked
        if not s or not words or not words[0]:
            return []
        stringlength = len(s)
        wordlength = len(words[0])
        totallength = len(words) * wordlength

        map = {}
        # store the occurrence of each word
        for word in words:
            map[word] = map[word] + 1 if word in map.keys() else 1

        result = []
        for i in range(min(wordlength, stringlength - wordlength + 1)):
            _findSubstring(i, i, stringlength, wordlength, totallength, s, map, result)

        return result
