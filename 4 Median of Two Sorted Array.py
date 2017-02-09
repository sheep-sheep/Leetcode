class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        # do the switch
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        lo = 0
        hi = m
        half = (m+n+1)/2

        while(lo <= hi):
            i = (lo + hi)/2
            j = half - i
            if i < m and nums2[j - 1] > nums1[i]:
                lo = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                hi = i - 1
            else:
                if i == 0:
                    maxofleft = nums2[j-1]
                elif j == 0:
                    maxofleft = nums1[i-1]
                else:
                    maxofleft = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return maxofleft

                if i == m:
                    minofright = nums2[j]
                elif j == n:
                    minofright = nums1[i]
                else:
                    minofright = min(nums1[i], nums2[j])

                return (maxofleft + minofright)/2.0

class Solution_1(object):

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


class Solution_2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = nums1 + nums2
        nums.sort()
        length = len(nums1) + len(nums2)
        if length%2 == 0:
            return (nums[length/2 - 1] + nums[length/2])/2.0
        else:
            return nums[length/2]
            
