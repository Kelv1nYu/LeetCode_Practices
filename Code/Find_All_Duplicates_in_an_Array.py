class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        
        for num in nums:
            # Use the original array as hash, then check if flag is negative
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                # Making elements at certain indexes (abs(num)-1) negative.
                nums[abs(num)-1] *= -1
        return res