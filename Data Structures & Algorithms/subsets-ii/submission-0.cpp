class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;

        sort(nums.begin(), nums.end());
        backtrack(0, nums, subset, res);

        return res;
    }

private:
    void backtrack(int idx, vector<int>& nums, vector<int>& subset, vector<vector<int>>& res) {
        if (nums.size() == idx) {
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[idx]);
        backtrack(idx + 1, nums, subset, res);
        subset.pop_back();

        while(idx + 1 < nums.size() && nums[idx] == nums[idx + 1]) idx++;
        backtrack(idx + 1, nums, subset, res);
    }
};
