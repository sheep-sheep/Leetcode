class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # for each bar, find the maxArea of the rectangle with current bar as the min height
        # however this solution can't handle the worst case
        # it's still doing the same thing and even worse.
        area = 0
        for idx in range(len(heights)):
            left = idx - 1
            right = idx + 1
            width = 1
            while (left >= 0 and heights[left] >= heights[idx]):
                width += 1
                left -= 1
            while (right <= len(heights) - 1 and heights[right] >= heights[idx]):
                width += 1
                right +=1
            area = max(area, width * heights[idx])
        return area

# this stack solution is recording the starting index and ending index
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
