class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> st;
        for (int n : nums) st.insert(n);
        // cout << st.size();
        if (st.size() != nums.size()) return true;
        return false;
    }
};