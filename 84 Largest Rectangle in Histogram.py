class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def maxMidArea(heights, left, mid, right):
            i = mid
            j = mid+1
            area = 0
            h = min(heights[i], heights[j]);
            while( i >= left and j <= right):
                h = min(h, heights[i], heights[j])
                area = max(area, (j-i+1)*h)
                if i == left:
                    j+=1
                elif j == right:
                    i-=1
                else:
                    # if left and right haven't reached boundary,
                    # choose the largest height side which will be
                    # more likely increase the area.
                    if heights[i-1] > heights[j+1]:
                        i -= 1
                    else:
                        j += 1
            return area

        def maxArea(heights, left, right):
            if left == right:
                return heights[left]*1

            mid = left + (right-left)/2
            leftArea = maxArea(heights, left, mid)
            rightArea = maxArea(heights, mid+1, right)
            midArea = maxMidArea(heights, left, mid, right)
            return max(leftArea, rightArea, midArea)

        if not heights:
            return 0
        return maxArea(heights, 0, len(heights)-1) #Typical binary search/divide and conquer
