class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = dict()
        maxFreq = 0
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] not in charCount:
                charCount[s[r]] = 0
            charCount[s[r]] += 1
            maxFreq = max(maxFreq, charCount[s[r]])

            if (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)  
        return ans


