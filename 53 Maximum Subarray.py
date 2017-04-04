class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        sum = 0
        for num in nums:
            if sum + num > sum:
                sum += num
            else:
                sum = 0
                res += [sum]
        return max(res)        
        
