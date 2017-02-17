class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '.*':
            return True
        tmp = None
        i = 0
        for char in s:
            if p[i] != '.':
                if p[i] != '*':
                    if p[i] != char:
                        return False
                else:
                    if tmp != char:
                        return False
                    else:
                        tmp = char
            else:
                tmp = char
            i += 1
        return True
