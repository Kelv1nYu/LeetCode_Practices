class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = -1
        for row in matrix:
            while j + len(row) >= 0 and row[j] > target:
                j -= 1
            if j + len(row) >= 0 and row[j] == target:
                return True
        
        return False