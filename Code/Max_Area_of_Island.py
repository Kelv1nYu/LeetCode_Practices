class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Set result
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                # If current index is 0 (water), keep searching
                if grid[i][j] == 0:
                    continue
                else:
                    # Start calculate area
                    area = self.dfs(grid, i, j)
                    # Check area and result
                    res = max(area, res)
        
        return res
    
    # DFS helper function
    def dfs(self, grid, i, j):
        """
        :type grid: List[List[int]]
        :type i: int
        :type j: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # Check boundary conditions and if current index is island
        if 0 <= i and i < m and 0 <= j and j < n and grid[i][j]:
            # Change island into water to avoid calculating area again
            grid[i][j] = 0
            # Use dfs to search up, down, left, and right
            return 1 + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)
        else:
            return 0