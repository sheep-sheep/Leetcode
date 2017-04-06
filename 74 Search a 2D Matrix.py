# Create a map to increase searching
# use binary search
# by my own

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binarySearch(nums, left, right, target):
            mid = left+(right - left)/2
            if mid < left:
                return mid
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    return binarySearch(nums,left,mid-1, target)
                else:
                    return binarySearch(nums, mid+1, right, target)

        if matrix and matrix[0]:
            width = len(matrix[0])
            height = len(matrix)
            map = []
            for row in range(height):
                map += [matrix[row][0]]
            rowIndex = binarySearch(map,0,height-1, target)
            colIndex = binarySearch(matrix[rowIndex],0,width-1, target)
            return matrix[rowIndex][colIndex] == target
        else:
            return False
