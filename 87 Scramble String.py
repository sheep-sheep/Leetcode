class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Prevent reaching max recursion depth
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False            
        # This is to check the base case when s1==s2
        if len(s1) < 4 or s1 == s2:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or\
               self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

# Since it's using recursion and build the result bottom up manner
# we can use memorization to reduce the calculation
    mem = {}
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if self.mem.get(s1+s2, False):
            return True
        # Prevent reaching max recursion depth
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        # This is to check the base case when s1==s2
        if len(s1) < 4 or s1 == s2:
            self.mem[s1+s2] = True
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.mem[s1[:i]+s2[:i]]= True
                self.mem[s1[i:]+s2[i:]]= True
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.mem[s1[:i]+s2[-i:]]= True
                self.mem[s1[i:]+s2[:-i]]= True
                return True
        return False
