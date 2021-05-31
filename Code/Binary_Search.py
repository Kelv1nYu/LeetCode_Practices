class Solution:
    def search(self, nums, target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # set the left and right boundary [left, right]
        left, right = 0, len(nums) - 1
        while left <= right:
            # find the mid index
            mid = left + (right - left) // 2
            # check the mid value and target
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1