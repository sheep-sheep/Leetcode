import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursivePermute(nums, lo, result):
            if lo >= len(nums)-1:
                result.append(copy.deepcopy(nums))
                return

            for i in range(lo, len(nums)):
                nums[i], nums[lo] = nums[lo], nums[i]
                recursivePermute(nums, lo+1, result)
                nums[i], nums[lo] = nums[lo], nums[i]
        result = []
        recursivePermute(nums, 0, result)
        return result
#Recursively shuffle the list to get the new permutation.

# it's the same idea with my 1st solution, however, mine failed!
# I should put the recursive under the iterative, try it later!
class Solution(object):
#Insert the first number anywhere in any permutation of the remaining numbers.
    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
    
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
        
        
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<2:
            return nums
        
        res = []
        for (idx,num) in enumerate(nums):
            for item in self.permute(nums[:idx]+nums[idx+1:]):
            	print idx, nums[:idx]+nums[idx+1:]
                tmp = [num]
                tmp.extend(item)
                res.append(tmp)
                print res
        
        return res

print Solution() .permute([1,2])        
