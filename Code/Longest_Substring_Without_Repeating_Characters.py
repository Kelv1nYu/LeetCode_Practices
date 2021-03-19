class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        ans = 0
        # mp stores the (current index) + 1 of a character
        mp = {}
        
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                # left border needs to move until the repeated characters move out of the left border
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        
        return ans