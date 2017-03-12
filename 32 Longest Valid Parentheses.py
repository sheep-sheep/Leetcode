class Solution(object):
    def longestValidParentheses(self, s):
         stack = [0]
         curr_max = 0
         s = ')'+s # create a invalid case for 0 index
         for i in range(1, len(s)):
             if s[i] == ')' and s[stack[-1]] == '(':
                 stack.pop()
                 curr_max = max(curr_max, i - stack[-1])
             else:
                 stack.append(i)
         return curr_max


# Time Limit Exceeded!!!    But my solution has the potential to print the longest string!
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        pq = {}
        i = 0
        if len(s) <2:
            return 0
        for parenth in s:
            if parenth == '(':
                pq[i] = '('
            else:
                if pq and pq[max(pq.keys())] == '(':
                    pq.pop(max(pq.keys()), None)
                else:
                    pq[i] = ')'
            i += 1
        result = []
        invalid = sorted(pq.keys())
        if invalid:
            for i in range(len(invalid)):
                if i != 0:
                    result +=[invalid[i] - invalid[i-1] - 1]
            return max(invalid[0], max(result) if result else 0, len(s) - 1 - invalid[-1])
        else:
            return len(s)
