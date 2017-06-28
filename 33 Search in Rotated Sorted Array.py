
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return -1
        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
        def binary(nums, left, right, target):
            if left > right:
                return -1
            if nums[(right - left) / 2 + left] == target:
                return (right - left) / 2 + left
            elif nums[(right - left) / 2 + left] < target:
                return binary(nums, (right - left) / 2 + left + 1, right, target)
            elif nums[(right - left) / 2 + left] > target:
                return binary(nums, left, (right - left) / 2 + left - 1, target)

        if target == nums[pivot]:
            return pivot
        elif target > nums[-1]:
            return binary(nums, 0, pivot, target)
        else:
            return binary(nums, pivot + 1, len(nums) - 1, target)
