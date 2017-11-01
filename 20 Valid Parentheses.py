class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        holder_0 = []
        holder_1 = []
        for symbol in s:
            if symbol in ('(', '{', '['):
                holder_0.append(symbol)
                while (holder_0 and holder_1):
                    if (holder_0[-1] == '[' and holder_1[-1] == ']') or \
                            (holder_0[-1] == '{' and holder_1[-1] == '}') or \
                            (holder_0[-1] == '(' and holder_1[-1] == ')'):
                        holder_0.pop()
                        holder_1.pop()
                    else:
                        return False
            if symbol in ('}', ']', ')'):
                holder_1.append(symbol)
                while (holder_0 and holder_1):
                    if (holder_0[-1] == '[' and holder_1[-1] == ']') or \
                            (holder_0[-1] == '{' and holder_1[-1] == '}') or \
                            (holder_0[-1] == '(' and holder_1[-1] == ')'):
                        holder_0.pop()
                        holder_1.pop()
                    else:
                        return False
        return holder_0 == [] and holder_1 == []

# Damn, why did i use such dump method?
# check my current implementation, i truely learnt sth right?

class Solution(object):
    def isValid(self, s):
        if s == '':
            return False
        
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if stack:
                    last = stack.pop()
                    if (last == '[' and char != ']') or (last == '(' and char != ')') or (last == '{' and char != '}'):
                        return False
                else:
                    return False
        return len(stack)==0
