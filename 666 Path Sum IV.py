class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        depth = {}
        positions = {}
        values = {}
        for num in nums:
            depth[num / 100] = depth[num / 100] + [num / 100] if num / 100 in depth.keys() else [num / 100]
            positions[num / 100] = positions[num / 100] + [num / 10 % 10] if num / 100 in positions.keys() else [
                num / 10 % 10]
            values[num / 100 * 10 + num / 10 % 10] = num

        def dfs(node, nums):
            # leaf
            if node / 100 == depth.keys()[-1]:
                return node % 10
            if node not in nums:
                return 0
            left = dfs(node/100*100+ (node / 100 + 1) * 10 + (node / 10 % 10) * 2, nums)
            right = dfs(node/100*100 + (node / 100 + 1) * 10 + (node / 10 % 10) * 2 + 1, nums)
            return node % 10 + left + right

        return dfs(nums[0], nums)

# Overall idea is correct but i made a mistake at summing part
