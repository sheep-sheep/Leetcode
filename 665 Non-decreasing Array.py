class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def isNonDecreasing(nums):
            count = 0
            for idx in range(len(nums) - 1):
                if nums[idx] > nums[idx + 1]:
                    if idx == 0:
                        nums[idx] = nums[idx + 1]
                        count += 1
                    elif idx == len(nums) - 2:
                        nums[idx + 1] = nums[idx]
                        count += 1
                    else:
                        nums[idx + 1] = min(nums[idx], nums[idx + 1]) if min(nums[idx], nums[idx + 1]) >= nums[idx-1] else max(nums[idx], nums[idx + 1])# make the change; repeat current number is the safest modification
                        count += 1

                    if count > 1:
                        return False
            return True

        return isNonDecreasing(nums)

