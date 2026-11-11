class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> subset;

        dfs(0, nums, subset, res, target, 0);
        return res;
    }

private:
    void dfs(int idx, vector<int>& nums, vector<int>& subset, vector<vector<int>>& res, int target, int total) {
        if (total == target) {
            res.push_back(subset);
            return;
        }

        if (idx >= nums.size() || total > target) return;

        subset.push_back(nums[idx]);
        dfs(idx, nums, subset, res, target, total + nums[idx]);

        subset.pop_back();
        dfs(idx + 1, nums, subset, res, target, total);
    }
};
