class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        nums.sort()
        self.backTrack(nums, 0, [], res)
        return res

    def backTrack(self, nums, pos, path, res):
        res.append(path)
        for i in range(pos, len(nums)):
            self.backTrack(nums, i+1, path +[nums[i]], res)
