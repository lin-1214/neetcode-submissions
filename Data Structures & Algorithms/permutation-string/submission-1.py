class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        windowSize = len(s1)
        if (windowSize > len(s2)):
            return False

        wordCount = [0] * 26
        for i in range(windowSize):
            idx = ord(s1[i]) - ord('a')
            wordCount[idx] += 1

        windowCount = [0] * 26
        l = 0
        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            if (r - l + 1) <= windowSize:
                windowCount[idx] += 1

            else:
                windowCount[ord(s2[l]) - ord('a')] -= 1
                windowCount[idx] += 1
                l += 1

            if (windowCount == wordCount):
                    return True
        return False