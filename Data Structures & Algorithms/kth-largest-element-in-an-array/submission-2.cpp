class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        this->k = k;
        for (auto num:nums) {
            pq.push(num);
            if (pq.size() > k) pq.pop();
        }

        return pq.top();
    }

private:
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
};
