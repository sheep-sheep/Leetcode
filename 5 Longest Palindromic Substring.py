class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
            
        s_len = len(s)
        largest = s_len
    
        while(largest != 1):
            result0 = result1 = []
            for i in range(0, s_len/2):
                if i + largest <= s_len:
                    #print 'Test', i, 'largest', largest, s[i:i+largest]
                    flag = self.isPalindrome(s[i:i+largest])
                    if flag:
                        result0 = s[i:i+largest]
    
            for i in range(s_len/2, s_len):
                if i + largest <= s_len:
                    #print 'Test', i, 'largest', largest, s[i:i+largest]
                    flag = self.isPalindrome(s[i:i+largest])
                    if flag:
                        result1 = s[i:i+largest]
                        
            if len(result0) !=0 and len(result1)!=0:
                if len(result0) > len(result1):
                    return result0
                else:
                    return result1
    
            if len(result0) != 0:
                return result0
            if len(result1) != 0:
                return result1
    
            largest = largest - 1
    
    def isPalindrome(self, s):
        '''
        Doesn't handle the length 1 and length 0
        '''
        s_len = len(s)
        if len(s)%2==0:
            #print 'Test Even', s
            return self.isPalindromeEven(s)
        else:
            s = s[:s_len/2]+s[s_len/2+1:]
            #print 'Test Odd', s
            return self.isPalindromeEven(s)
    
    def isPalindromeEven(self, s):
        if len(s) == 2:
            if s[0] != s[1]:
                return False
            else:
                return True
        if s[0] != s[-1]:
            return False
        else:
            return self.isPalindromeEven(s[1:-1])
        
