class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # the correct way should be find the relationship between n=2
        # and n=3

        # the algorith will be appending 1 or 0 to the previous list
        
        # exponetional in python is **
        res = [0]
        for i in range(n):
            size = len(res)
            for k in reversed(range(size)):
                res.append(2**i * 1 + res[k])
        return res

    
    
    # 2**i can be replaced by 1<<i; and + can be replaced by |
