class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        for i in range(len(nums)-1, -1, -1):
            right = i
            left = i -1
            if left == 0 and nums[left] > nums[right]:
                nums.sort()
                return
            if nums[left] < nums[right]:
                break
        right = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[left]:
                right = i
                break
        nums[left], nums[right] = nums[right], nums[left]
        self.reverse(nums, left + 1, len(nums) - 1)

    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
# The part I missed was to reverse the array between left and the end.

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

# i need to update this too
