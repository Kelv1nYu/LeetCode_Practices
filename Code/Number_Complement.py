class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bnum = '{0:b}'.format(num)
        temp = int(len(bnum) * '1') - int(bnum)
        dnum = int(str(temp),2)
        return dnum