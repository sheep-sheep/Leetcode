class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m and n:
            for pos in range(m+n-1, -1, -1):
                if nums1[m-1]>nums2[n-1] and m-1>=0:
                    nums1[pos] = nums1[m-1]
                    m -= 1
                elif nums1[m-1]<=nums2[n-1] and n-1>=0:
                    nums1[pos] = nums2[n-1]
                    n -= 1
                elif m-1 < 0:
                    nums1[pos] = nums2[n-1]
                    n -= 1
        elif m ==0 and n != 0:
            for pos in range(n-1, -1, -1):
                nums1[pos] = nums2[pos]
                
                
# wow, i can't believe i can solove them so quickly!                
