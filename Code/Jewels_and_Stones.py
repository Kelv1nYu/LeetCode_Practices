class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ## Solution 1
        count = 0
        for element in S:
            if element in J:
                count += 1

        return count

        ## Solution 2
        Jset = set(J)
        return sum(s in Jset for s in S)