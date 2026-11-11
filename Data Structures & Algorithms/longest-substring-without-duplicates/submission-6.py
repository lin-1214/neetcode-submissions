class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charLookup = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in charLookup and charLookup[s[r]] >= l:
                l = charLookup[s[r]] + 1
            charLookup[s[r]] = r

            ans = max(ans, r - l + 1)


        return ans


             