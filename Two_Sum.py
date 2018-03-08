class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rest = dict()
        # result = list()


        for index in range(len(nums)):
            if nums[index] not in rest.keys():
                rest[target - nums[index]] = index
            else:
                # result.append(rest[nums[index]])
                # result.append(index)
                return [rest[nums[index]], index]

        # return result