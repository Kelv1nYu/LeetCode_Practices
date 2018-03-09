class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        result = list()

        for num in range(left, right + 1):
            count = 0
            snum = str(num)
            for item in snum:
                if int(item) != 0:
                    if num % int(item) == 0:
                        count += 1
                    else:
                        break
            if count == len(snum):
                result.append(num)

        return result