class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def search(low, high, target, nums):
        	mid = (high + low)/2
        	if low > high:
        		return [-1, -1]
        	if nums[mid] == target and low <= high:
        		result = mid
        		while result + 1 <= len(nums)-1 and nums[result+1] == target:
        			result += 1
        		result1 = mid
        		while result1 - 1 >= 0 and nums[result1-1] == target:
        			result1 -= 1
        		return [min(result, result1), max(result1, result)]
        	elif nums[mid] < target:
        		return search(mid+1, high, target, nums)
        	elif nums[mid] > target:
        		return search(low, mid-1, target, nums)

        return search(0, len(nums)-1, target, nums)
