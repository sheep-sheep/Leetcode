class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        return len(s.split(' ')[-1]) if s.split(' ')[-1]!='' else 0

# jianchao.li.fighter 
# Reputation:  4,277
# Well, the basic idea is very simple. Start from the tail of s and move backwards to find 
# the first non-space character. Then from this character, move backwards and count the number 
# of non-space characters until we pass over the head of s or meet a space character. The count 
# will then be the length of the last word.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        tail = len(s) - 1
        while (tail >= 0 and s[tail] == ' '):
            tail -=1
        while (tail >= 0 and s[tail] != ' '):
            length+=1
            tail-=1
        return length
        
