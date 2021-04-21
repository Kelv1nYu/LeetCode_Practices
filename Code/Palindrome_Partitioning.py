class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        # Call dfs function
        self.dfs(s, [], res)
        
        return res
    
    def dfs(self, s, path, res):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # If the string is empty, it means that the partition is over and the path will be added to the result array
        if not s:
            res.append(path)
            return
        
        # Partition the string from the beginning
        for i in range(1, len(s) + 1):
            # Only the current string is a palindrome will partition the second part
            if self.isPar(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    
    def isPar(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Check whether the string is a palindrome
        return s == s[::-1]

# Backtracking
class Solution2:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Define the backtracking algorithm
        def backTracking(s, path, res):
            """
            :type s: str
            :type path: List[str]
            :type res: List[List[str]]
            """
            # If the string is empty, it means that the partition is over and the path will be added to the result array
            if not s:
                res.append(path[:])
                return
            
            # Partition the string from the beginning
            for i in range(1, len(s)+1):
                # Only the current string is a palindrome will partition the second part
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    backTracking(s[i:], path, res)
                    # After the current backtracking ends, it will backtrack to the previous loop,
                    # and at the same time pop out the data in the current backtracking loop saved in the path
                    path.pop()
        res = []
        backTracking(s, [], res)
        return res