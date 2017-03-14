


# 1st solution, i know the check part will need lots of time.
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursivePermute(nums, lo, result):
            if lo >= len(nums)-1:
                if nums not in result:
                    result.append(copy.deepcopy(nums))
                return
            for i in range(lo, len(nums)):
                nums[i], nums[lo] = nums[lo], nums[i]
                recursivePermute(nums, lo+1, result)
                nums[i], nums[lo] = nums[lo], nums[i]
        result = []
        recursivePermute(nums, 0, result)
        return result
