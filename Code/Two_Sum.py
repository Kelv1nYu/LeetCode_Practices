class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create dictionary for storing result
        res = dict()

        # Traverse the list
        for index in range(len(nums)):

            # Check if the value was stored in the dictionary as the key
            if nums[index] not in res.keys():
                # If False, use difference between the target and the value as the key, and the current index will be stored in the dictionary as the value
                res[target - nums[index]] = index
            else:
                # If True, return difference index and current index
                return [res[nums[index]], index]

        return None

