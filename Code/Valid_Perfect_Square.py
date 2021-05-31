class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        # set left and right boundary
        left, right = 0, num

        while left <= right:
            # get mid value
            mid = left + (right - left) // 2
            
            # check the square num and target num
            square_num = mid * mid
            if square_num > num:
                right = mid - 1
            elif square_num < num:
                left = mid + 1
            else:
                return True
        return False
        