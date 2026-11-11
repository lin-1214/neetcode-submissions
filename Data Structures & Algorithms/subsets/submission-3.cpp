class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        dfs(0, nums, subset, res);
        return res;
    }

private:
    void dfs(int idx, vector<int>& nums, vector<int>& subset, vector<vector<int>>& res) {
        if (idx >= nums.size()) {
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[idx]);
        dfs(idx+1, nums, subset, res);

        subset.pop_back();
        dfs(idx+1, nums, subset, res);
    }
};
