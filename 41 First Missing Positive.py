class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for index in xrange(n):
            element = nums[index]
            while True:
                if element <= 0 or element > n or element == nums[element - 1]:
                    break
            nums[element - 1], element = element, nums[element - 1]
        for index in xrange(n):
            if nums[index] != index + 1:
                return index + 1
        return n + 1
