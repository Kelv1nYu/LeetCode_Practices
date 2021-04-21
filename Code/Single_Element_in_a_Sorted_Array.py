class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2

            # Determine whether the current median value is equal to the left value or equal to the right value
            if nums[mid] == nums[mid+1]:
                # Determine whether the left and right parts of the current median are odd or even
                if (right - mid) % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 1

            # Determine whether the current median value is equal to the left value or equal to the right value
            elif nums[mid] == nums[mid-1]:
                # Determine whether the left and right parts of the current median are odd or even
                if (right - mid) % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            # If the median is unique, return the median
            else:
                return nums[mid]
        # If the loop stops, i.e. left == right, return this value
        return nums[left]