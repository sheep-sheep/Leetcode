class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def combineLetter(s, keys):
            if len(s) == 2:
                res = []
                for i in keys[s[0]]:
                    for j in keys[s[1]]:
                        res += [i+j]
                return res
            elif len(s) == 1:
                res = []
                for i in keys[s[0]]:
                    res += [i]
                return res
            else:
                return [x + y for x in combineLetter(s[:len(s)/2], keys) for y in combineLetter(s[len(s)/2:], keys)]

        keys = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z'],
                }
        digits = digits.replace('1', '')
        digits = digits.replace('0', '')

        if digits == '':
            return []

        res = combineLetter(digits, keys)
        return res
