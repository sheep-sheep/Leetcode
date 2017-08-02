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
    
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0] # make the stack not empty,
                                      # make the last one to be smallest height.
        ind_stack = [0] # 2nd stack to save index of height
        area = 0
        for i in range(1, len(heights)):
            while(heights[i]<heights[ind_stack[-1]]):
                prev_ind = ind_stack.pop()
                area = max(area, heights[prev_ind]*(i-ind_stack[-1]-1))
            ind_stack.append(i)
        return area    
