class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        elif n == 2:
            return ['()()',
                    '(())',]
        else:
            final = {}
            for elem in self.generateParenthesis(n - 1):
                final[elem + '()'] = elem + '()'
                final['()' + elem] = '()' + elem
                final['(' + elem + ')'] = '(' + elem + ')'
            return final.keys()
# I really like the idea of my initial solution, however , it can't handle (())(()) such seperate case when n = 4            
