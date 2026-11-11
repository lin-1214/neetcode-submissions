class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        vector<bool> pick(nums.size(), false);
        backtrack(nums, subset, res, pick);

        return res;
    }

private:
    void backtrack(vector<int>& nums, vector<int>& subset, vector<vector<int>>& res, vector<bool>& pick) {
        if (subset.size() == nums.size()) {
            res.push_back(subset);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!pick[i]) {
                subset.push_back(nums[i]);
                pick[i] = true;
                backtrack(nums, subset, res, pick);
                subset.pop_back();
                pick[i] = false;
            }
        }
    }
};
