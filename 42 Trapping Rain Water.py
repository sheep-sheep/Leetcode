class Solution(object):
    # Solution 1, it's TLE becuase of O(n^2)
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for (i, h) in enumerate(height):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            res += min(max_left, max_right) - h

        return res
