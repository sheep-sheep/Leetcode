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

    
# with indexes:
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax = [(0, 1)]*len(nums)
        endingMax = nums[0]
        sumMax = nums[0]
        for i in range(1, len(nums)):
            temp = endingMax+nums[i]
            endingMax = max(nums[i], temp)
            globalMax[i] = (i, i+1) if temp < nums[i] else (globalMax[i-1][0], globalMax[i-1][1]+1)
            sumMax = max(endingMax, sumMax)
        return nums[globalMax[-1][0]:globalMax[-1][1]]
