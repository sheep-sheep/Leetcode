class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        high = len(nums) - 1
        if high == -1:
            return -1
        else:
            while(lo < high):
            	mid = (lo+high)/2
            	if nums[mid] == target:
            		return mid
            	if nums[lo] <= nums[mid]:
            		if (nums[lo] <= target and nums[mid]> target):
            			high = mid - 1
            		else:
            			lo = mid + 1
            	else:
            		if (nums[high] >= target and nums[mid] < target):
            			lo = mid + 1
            		else:
            			high = mid  - 1
            return lo if nums[lo] == target else -1
