class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # Call dfs function
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, candidates, target, path, res):
        """
        :type candidates: List[int]
        :type target: int
        :type path: List[int]
        :type res: List[List[int]]
        """
        # if target < 0, it means current sum is greater than target, then return
        if target < 0:
            return

        # if target = 0, which means current sum equals target, then add path to result array
        if target == 0:
            res.append(path)
            return
        
        # Each cycle starts from the first number of original array
        # Change to the next number until the current sum exceeds the target
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)

# Backtracking
class Solution2:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # call Backtracking function
        def backTracking(target, path, start):
            # exceed the scope, stop exploration.
            if target < 0:
                return
            if target == 0:
                # make a shallow copy of the current combination
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # add the number into the combination
                path.append(candidates[i])
                # give the current number another chance, rather than moving on
                backTracking(target - candidates[i], path, i)
                # backtrack, remove the number from the combination
                path.pop()
        
        path = []
        backTracking(target, path, 0)
        return res