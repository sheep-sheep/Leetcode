#Failed solution
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursivePermute(num1, nums2):
            if len(nums2) == 1:
                return [[num1, nums2[0]], [nums2[0], num1]]
            else:
                result = []
                tmp = recursivePermute(nums2[0], nums2[1:])
                for i in range(len(tmp) + 1):
                    tmp2 = copy.deepcopy(tmp)
                    for num in tmp2:
                        num.insert(i, num1)
                        result += [num]
                return result
        if len(nums) >= 2:
            return recursivePermute(nums[0], nums[1:])
        else:
            return [nums] if nums else []
