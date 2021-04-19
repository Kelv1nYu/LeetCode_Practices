class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0])
        
        if m == 0:
            return False
        
        # Set the left and right borders
        left, right = 0, m * n - 1
        
        # Binary search
        while left <= right:
            mid = left + (right - left) // 2
            # Change one-dimensional array subscript to two-dimensional array subscript
            ele = matrix[mid // n][mid % n]

            # Adjust the left and right borders
            if target == ele:
                return True
            else:
                if target < ele:
                    right = mid - 1
                else:
                    left = mid + 1
        return False