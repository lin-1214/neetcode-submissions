class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tCount = dict()
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        need = len(tCount)
        have = 0

        windowCount = dict()
        l = 0
        bestLen = float('inf')
        bestLeft, bestRight = 0, 0

        for r in range(len(s)):
            c = s[r]
            windowCount[c] = windowCount.get(c, 0) + 1

            if c in tCount and windowCount[c] == tCount[c]:
                have += 1

            while have == need:
                # record answer if this window is shorter
                if (r - l + 1) < bestLen:
                    bestLen = r - l + 1
                    bestLeft, bestRight = l, r

                # shrink from the left
                leftChar = s[l]
                windowCount[leftChar] -= 1
                if leftChar in tCount and windowCount[leftChar] == tCount[leftChar] - 1:
                    have -= 1
                l += 1

        if bestLen == float('inf'):
            return ""
        return s[bestLeft:bestRight + 1]