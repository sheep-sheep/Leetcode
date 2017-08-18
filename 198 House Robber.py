class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)  
        return now
        


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, (len(nums) + 1)):
            dp[i] = max(nums[i-1] + dp[i - 2], dp[i - 1])
        return dp[-1]
    
    I need a better explaination about the index number!!!!!
