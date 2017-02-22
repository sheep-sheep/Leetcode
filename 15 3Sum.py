class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip the same fixed position
            
            lo, hi = i + 1, len(nums) - 1 # 2 pointers to narrow down the list
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return res


# My initial solution, use O(n*n) + a binary search to find the target.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        hi = len(nums)
        i = 0
        j = 1
        final = {}
        while((nums[i] + nums[j] <= 0) and nums[i] <= 0 and nums[j] <= 0):
            result = binary_search(j+1, hi, -(nums[i] + nums[j]))
            if (nums[i])
            i += 1
            j += 1
