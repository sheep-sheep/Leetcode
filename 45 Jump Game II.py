class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        level = 0
        currMax = 0
        nextMax = 0
        i = 0
        while(currMax-i+1>0):
            level+=1
            while(i<=currMax):
                nextMax = max(nextMax, nums[i] + i)
                if nextMax >= len(nums) - 1:
                    return level
                i += 1
            currMax = nextMax
        return 0
