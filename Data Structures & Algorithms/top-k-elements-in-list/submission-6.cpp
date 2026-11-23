class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;

        for (int n : nums) {
            cnt[n]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> max_heap;

        for (auto& [n, count] : cnt) {
            max_heap.push({count, n});
            if (max_heap.size() > k) {
                max_heap.pop();
            }
        }

        vector<int> ans;

        for (int i = 0; i < k; i++) {
            ans.push_back(max_heap.top().second);
            max_heap.pop();
        }

        return ans;
    }
};
