class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        candid = []
        ans = 0

        if len(nums) == 0:
            return 0

        for num in nums:
            lookup.add(num)

        for num in lookup:
            if (num-1) in lookup:
                continue
            else:
                candid.append(num)

        for num in candid:
            tmp = 1
            ans = max(ans, tmp)
            while (num+1) in lookup:
                tmp += 1
                ans = max(ans, tmp)
                num += 1

        return ans

        