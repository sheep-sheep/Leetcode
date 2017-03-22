class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        maxjump=0
        for i in range(len(nums)):
            maxjump=max(maxjump-1,nums[i])
            if maxjump==0:
                break
        
        return i==len(nums)-1
