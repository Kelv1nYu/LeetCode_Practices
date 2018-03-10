class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums = nums[::2]
        tot = 0
        for num in nums:
            tot += num
        return tot