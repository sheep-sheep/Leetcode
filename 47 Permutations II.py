# My successful solution:
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums):
            if len(nums) == 2:
                return [[nums[1], nums[0]], [nums[0], nums[1]]] if nums[1]!=nums[0] else [nums]
            elif len(nums) < 2:
                return [nums]
            else:
                count = 0
                tmp = []
                prev = None
                for num in nums:
                    if prev != num:
                        prev = num
                    else:
                        count +=1
                        continue
                    for candidate in dfs(nums[0:count]+nums[count+1:]):
                        tmp.append([num]+candidate)
                    count +=1
                return tmp
        return dfs(sorted(nums))


import copy
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursivePermute(nums, lo, result):
            nums = copy.deepcopy(nums)
            if lo >= len(nums)-1:
                result.append(nums)
                return
            for i in range(lo, len(nums)):
                if i!=lo and nums[i] == nums[lo]:
                    continue
                nums[i], nums[lo] = nums[lo], nums[i]
                recursivePermute(nums, lo+1, result)
        result = []
        nums = sorted(nums)
        recursivePermute(nums, 0, result)
        return result
# Get it from Permutaion I, python has its own pass by reference and pass by value!


# 1st solution, i know the check part will need lots of time.
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursivePermute(nums, lo, result):
            if lo >= len(nums)-1:
                if nums not in result:
                    result.append(copy.deepcopy(nums))
                return
            for i in range(lo, len(nums)):
                nums[i], nums[lo] = nums[lo], nums[i]
                recursivePermute(nums, lo+1, result)
                nums[i], nums[lo] = nums[lo], nums[i]
        result = []
        recursivePermute(nums, 0, result)
        return result
