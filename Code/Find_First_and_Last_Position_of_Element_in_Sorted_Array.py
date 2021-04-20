class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use binary search variant algorithm
        return [self.searchFirstEqualElement(nums, target), self.searchLastEquaElement(nums, target)]
    
    # Find the element whose first value is equal to the given value
    def searchFirstEqualElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            
            # Check whether the same value exists before the current value
            else:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    r = mid - 1
        return -1
    
    # Find the element whose last value is equal to the given value
    def searchLastEquaElement(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # Check whether the same value exists after the current value
                if mid == len(nums) - 1 or nums[mid+1] != target:
                    return mid
                else:
                    l = mid + 1
        return -1
        