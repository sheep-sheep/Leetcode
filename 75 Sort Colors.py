class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for num in range(len(nums)):
            tmp = nums[num]
            nums[num] = 2
            if tmp < 2:
                nums[j] = 1
                j += 1
            if tmp == 0:
                nums[i] = 0
                i += 1
                
