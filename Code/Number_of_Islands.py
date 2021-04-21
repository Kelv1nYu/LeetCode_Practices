class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                # if find island, call dfs function to check up, down, left and right
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # count island
                    cnt += 1
        
        return cnt
    
    def dfs(self, grid, i, j):
        """
        :type grid: List[List[int]]
        :type i: int
        :type j: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # check if current index is island
        if i < 0  or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        
        # set flag # as found island
        grid[i][j] = '#'
        
        # DFS
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)