class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        suffix = []
        l = n-2
        r = -1
        ans = []

        tmp = 1
        for i in range(n - 1):
            tmp *= nums[i]
            prefix.append(tmp)

        tmp = 1
        for i in range(n-1, 0, -1):
            tmp *= nums[i]
            suffix.append(tmp)

        for i in range(n):
            if i == 0:
                ans.append(suffix[l])
                
            elif i == (n-1):
                ans.append(prefix[r])
                
            else:
                ans.append(suffix[l] * prefix[r])
                
            l -= 1
            r += 1

        return ans