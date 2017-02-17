class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I'm treating 'IV' as a whole number, 
        # in fact, we don't need to, 
        # just subtract the 'I' will give us the same result.
        map = { 'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        num = 0
        i = 0
        if len(s) == 1:
            return map[s[i]]
        while i < len(s) - 1:
            if map[s[i]] < map[s[i+1]]:
                num += map[s[i+1]] - map[s[i]]
                i += 2
            else:
                num += map[s[i]]
                i += 1
        if i == len(s) - 1:
            num += map[s[i]]
        return num

class Solution1(object):        
    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]        
