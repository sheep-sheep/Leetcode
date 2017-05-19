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

    
# with indexes, i guess we have to remember this kind of format now
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        optimalMax = nums[0]
        optDP = (0, 1)
        globlaMax = nums[0]
        globalDP = (0, 1)
        for i in range(1, len(nums)):
            optDP = (i, i + 1) if optimalMax < 0 else (optDP[0], i + 1)
            optimalMax = max(nums[i], nums[i] + optimalMax)

            globalDP = optDP if optimalMax > globlaMax else globalDP
            globlaMax = max(optimalMax, globlaMax)
        return sum(nums[globalDP[0]: globalDP[1]])
