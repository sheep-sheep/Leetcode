class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

# we don't need to use DP or this is already a DP solution.    
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax = nums[0]
        endingMax = nums[0]

        for i in range(1, len(nums)):
            endingMax = max(nums[i], endingMax+nums[i])
            globalMax = max(endingMax, globalMax)

        return globalMax
