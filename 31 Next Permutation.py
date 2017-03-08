class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        def nextPermu(left, right, nums, minNumIndex):
            if left == 0:
                if nums[left] > nums[minNumIndex] and nums[left] >= nums[right]:
                    nums.sort()
                    return
                elif nums[left] <= nums[minNumIndex]:
                    nums[left], nums[right], nums[minNumIndex] = nums[minNumIndex], nums[left], nums[right]
                    return
            elif nums[left] < nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                return
            else:
                minNumIndex = right - 1 if nums[right - 1] < nums[minNumIndex] else minNumIndex
                nextPermu(left - 1, right - 1, nums, minNumIndex)

        nextPermu(len(nums)-2, len(nums) - 1, nums, len(nums)-2 if nums[len(nums)-2] < nums[len(nums) - 1] else len(nums) - 1)
        print nums

Solution().nextPermutation([2, 3, 1])
