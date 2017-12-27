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

    # Solution 2, use DP to reduce the loop to get height
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = 0
        max_left = [0] * (len(height) + 1)
        max_right = [0] * (len(height) + 1)
        for i in range(1, len(height)+1):
            max_left[i] = max(max_left[i-1], height[i-1])
        max_right[len(height)] = height[-1]
        for i in range(len(height)-1, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        for (i, h) in enumerate(height):
            res += min(max_left[i+1], max_right[i]) - h

        return res
    
    # Solution 3, only pass once to check 2 directions.
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
