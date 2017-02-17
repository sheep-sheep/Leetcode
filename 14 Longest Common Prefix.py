class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        result = ''
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]
        for char in strs[0]:
            flag = False
            for str in strs[1:]:
                # handle out of index
                if i < len(str) and char == str[i] :
                    flag = True
                else:
                    flag = False
                    break
            i += 1
            if flag:
                result += char
            else:
                break
        return result
