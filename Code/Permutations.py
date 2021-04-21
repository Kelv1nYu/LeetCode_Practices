class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # call dfs function
        # Incoming parameters: Original array, Array of each permutation, Reault array
        self.dfs(nums, [], res)
        
        return res
    
    def dfs(self, nums, path, res):
        """
        :type nums: List[int]
        :type path: List[int]
        :type res: List[List[int]]
        """
        # If all the numbers in the array are taken out, the recursion ends, and the current permutation will be stored in the result array
        if not nums:
            res.append(path)
        
        # Take the numbers from the array in turn
        # Put the number into the path array, and pass the remaining numbers into the next layer of recursive
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        
        # Take the numbers from the array one by one
        for n in nums:
            new_perms = []

            # Copy the perm array and add the newly taken number into it
            for perm in perms:
                
                for i in range(len(perm) + 1):
                    # Select the insertion position according to the number of existing numbers
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        
        return perms