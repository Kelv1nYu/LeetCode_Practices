class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :retype: int
        """

        left, right = 0, len(nums) - 1

        # Binary Search
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # check if the mid number is less than or equal the right one
            elif nums[mid] <= nums[right]:
                # check if target between nums[mid] and nums[right]
                if nums[mid] < target and target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # if nums[mid] > nums[right], then check if target between nums[mid] and nums[left]
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1