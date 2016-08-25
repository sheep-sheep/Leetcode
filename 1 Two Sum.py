class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        for i in nums:
            count = count + 1
            for j in nums[count:]:
                if i + j == target:
                    return [nums.index(i), nums[count:].index(j)+count]
