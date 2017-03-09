class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(nums, left, right, target, flag):
            flag[left] = True
            flag[right] = True
            if nums[(left + right)/2] == target:
                return (left + right)/2
            elif nums[(left + right)/2] > target:
                if flag[(left + right)/2]:
                    return (left + right)/2
                return search(nums, left, (left + right)/2, target, flag)
            elif nums[(left + right)/2] < target:
                if flag[(left + right)/2]:
                    return right
                return search(nums, (left + right) / 2, right, target, flag)
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        else:
            if target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                flag = [False]*len(nums)
                return search(nums, 0, len(nums)-1, target, flag)
