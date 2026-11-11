class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        tmp = []

        def dfs(i, remain):
            if (remain == 0):
                ans.append(tmp[:])
                return

            if (remain < 0):
                return

            for j in range(i, len(nums)):
                tmp.append(nums[j])
                dfs(j, remain - nums[j])
                tmp.pop()

        dfs(0, target)
        return ans

