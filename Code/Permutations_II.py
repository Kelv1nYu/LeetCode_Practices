class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # Sort the array for easy deduplication
        nums.sort()
        # Call dfs function
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
            # If the current number is the same as the previous number in the original array, skip this loop
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)


# Backtracking (Not recommended)
import copy
class Solution2:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Set flag for every number
        used = [False for _ in range(len(nums))]
        def backtrack(path, used, depth, output):
            if depth == len(nums):
                # Deepcopy (Can be omitted)
                newpath = copy.deepcopy(path)
                # Prevent duplication
                if newpath not in output:
                    output.append(newpath)
            
            for i in range(len(nums)):
                # Check if the number is taken out
                if not used[i]:
                    # Append number
                    path.append(nums[i])
                    # Change flag
                    used[i] = True
                    # Go to next layer
                    backtrack(path, used, depth+1, output)
                    # Reset flag
                    used[i] = False
                    # Pop current number from path
                    path.pop()
        path = []
        depth = 0
        output = []  
        backtrack(path, used, depth, output)
        return output