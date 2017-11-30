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
                
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, blue = 0, -1
        for i in range(len(nums)):
            while nums[i] == 2 and i < len(nums)+blue:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
            while nums[i] == 0 and i > red:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
