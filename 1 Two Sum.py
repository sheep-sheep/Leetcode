class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        for i in nums:
            count = count + 1
            for j in nums[count:]:
                if i + j == target:
                    return [nums.index(i), nums[count:].index(j)+count]

    def twoSum_hash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        searchdict = {}
        count = 0
        for i in nums:
            searchdict[i] = count
            count = count + 1
        count = 0
        for i in nums:
            num = target - i
            try:
                index = searchdict[num]
                if index != count:
                    return [count, index]
            except KeyError:
                pass
            count = count + 1
            
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}
        count = 0
        for num in nums:
            numsMap[num] = count
            count += 1
        count = 0
        for num in nums:
            ans = numsMap.get(target-num, None)
            if ans:
                return [count, ans]
            count += 1         
