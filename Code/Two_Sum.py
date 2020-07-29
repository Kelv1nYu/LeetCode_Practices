class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create dictionary for storing result
        rest = dict()


        for index in range(len(nums)):
            if nums[index] not in rest.keys():
                rest[target - nums[index]] = index
            else:
                return [rest[nums[index]], index]

        return None
