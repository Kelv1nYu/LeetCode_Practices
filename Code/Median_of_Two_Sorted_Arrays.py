class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # check the length of two arrays, and use the shorter array as nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        
        low, high, k, nums1Mid, nums2Mid = 0, m, (m + n + 1) // 2, 0, 0

        # generate mid line A and mid line B, then make the numbers on the left side of the line are less than the numbers on the right side
        while low <= high:
            nums1Mid = low + (high - low) // 2
            nums2Mid = k - nums1Mid

            if nums1Mid > 0 and nums1[nums1Mid - 1] > nums2[nums2Mid] :
                high = nums1Mid - 1
            elif nums1Mid != m and nums1[nums1Mid] < nums2[nums2Mid - 1]:
                low = nums1Mid + 1
            else:
                break
        
        # Calculate the median by the elements on the left and right sides of the mid lines
        midLeft, midRight = 0, 0
        if nums1Mid == 0:
            midLeft = nums2[nums2Mid - 1]
        elif nums2Mid == 0:
            midLeft = nums1[nums1Mid - 1]
        else:
            midLeft = max(nums1[nums1Mid - 1], nums2[nums2Mid - 1])
        
        if (m + n) % 2 == 1:
            return float(midLeft)
        if nums1Mid == m:
            midRight = nums2[nums2Mid]
        elif nums2Mid == n :
            midRight = nums1[nums1Mid]
        else:
            midRight = min(nums1[nums1Mid], nums2[nums2Mid])
        
        return float(midLeft + midRight) / 2