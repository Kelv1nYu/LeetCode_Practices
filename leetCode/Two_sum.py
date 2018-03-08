

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rest = dict()
        result = list()

        for num in nums:
            if target - num != num:
                rest[target - num] = num


        for index in range(len(nums)):
            if nums[index] not in rest.keys():
                continue
            else:
                result.append(index)


        return result