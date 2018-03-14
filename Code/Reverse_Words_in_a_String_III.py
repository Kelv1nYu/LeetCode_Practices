class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = " "
        strings = s.split()[::-1]
        for string in strings:
            result = result + string[::-1] + " "
        return result.strip()