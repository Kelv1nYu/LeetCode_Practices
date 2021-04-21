class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        # Count the characters that appear in the T string separately
        # Can also use count = collections.Counter(T), then the value of count[letter] is the number of occurrences
        tmp = dict()
        for letter in T:
            tmp[letter] = tmp.get(letter, 0) + 1
        
        # Fill the result with the characters in the order in which they appear in the S string
        for letter in S:
            if letter in T:
                res += letter * tmp[letter]
        
        # Add the remaining characters to the result
        for letter in T:
            if letter not in S:
                res += letter
        
        return res
        