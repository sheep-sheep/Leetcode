class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def merge(l1, l2):
            if len(l1) == 0 or len(l2) == 0:
                return l1 + l2
            if len(l1) == 1 and len(l2) == 1:
                if l1[0] < l2[0]:
                    return l1 + l2
                else:
                    return l2 + l1
            else:
                if l1[0] < l2[0]:
                    return [l1[0]] + merge(l1[1:], l2)
                else:
                    return [l2[0]] + merge(l1, l2[1:])
                    
        result = merge(nums1, nums2)
        num = len(result)
        
        if num%2 == 0:
            return (result[num/2] + result[num/2 - 1])/2.0
        else:
            return result[num/2]
        
