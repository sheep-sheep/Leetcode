class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # Swap the last k elements with the first k elements.
        # The last k elements will be in the correct positions
        # but we need to rotate the remaining (n - k) elements
        # to the right by k steps.
        print k
        k = k%len(nums)
        for i in range(k):
            nums[i], nums[len(nums)-k+i] = nums[len(nums)-k+i], nums[i]
        print nums
        # print k
        # for i in range(k):
        #     start = k+i
        #     end = len(nums)-k+i
        #     print nums
        #     for j in range(end, start, -1):
        #         nums[j], nums[j-1] = nums[j-1], nums[j]
        # print nums
