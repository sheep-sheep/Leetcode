class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h) 
            waterLevel += [left] # over-fill it to left max height
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
        return sum(waterLevel)
