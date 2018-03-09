class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = '{0:b}'.format(x)
        by = '{0:b}'.format(y)

        if len(bx) > len(by):
            by = '0' * (len(bx) - len(by)) + by
        else:
            bx = '0' * (len(by) - len(bx)) + bx

        count = 0
        for index in range(len(bx)):
            if bx[index] != by[index]:
                count += 1

        return count