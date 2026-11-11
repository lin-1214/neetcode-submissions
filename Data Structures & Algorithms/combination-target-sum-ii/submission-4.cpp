class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> subset;

        sort(candidates.begin(), candidates.end());
        dfs(0, candidates, subset, res, target, 0);
        return res;
    }

private:
    void dfs(int idx, vector<int>& candidates, vector<int>& subset, vector<vector<int>>& res, int target, int total) {
        if (total == target) {
            res.push_back(subset);
            return;
        }

        if (idx >= candidates.size() || total > target) return;

        subset.push_back(candidates[idx]);
        dfs(idx + 1, candidates, subset, res, target, total + candidates[idx]);

        subset.pop_back();
        while(idx+1 < candidates.size() && candidates[idx] == candidates[idx+1]) idx++;
        dfs(idx + 1, candidates, subset, res, target, total);
    }
};
