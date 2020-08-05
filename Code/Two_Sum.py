class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create dictionary for storing result
        rest = dict()

        # Traverse the list
        for index in range(len(nums)):

            # Check if the value was stored in the dictionary as the key
            if nums[index] not in rest.keys():
                # If False, use difference between the target and the value as the key, and the current index will be stored in the dictionary as the value
                rest[target - nums[index]] = index
            else:
                # If True, return difference index and current index
                return [rest[nums[index]], index]

        return None
