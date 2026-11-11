class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []
        tmp = []

        def dfs(i, remain):
            if remain == 0:
                ans.append(tmp[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if remain < candidates[j]:
                    continue
                tmp.append(candidates[j])
                dfs(j+1, remain - candidates[j])
                tmp.pop()



        dfs(0, target)
        return ans