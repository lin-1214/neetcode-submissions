class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto comp = [](const vector<int>& a, const vector<int>& b) {
            return a[0]*a[0] + a[1]*a[1] < b[0]*b[0] + b[1]*b[1];
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(comp)> pq(comp);
        
        for (auto point:points) {
            pq.push({point[0], point[1]});
            if (pq.size() > k) pq.pop();
        }

        vector<vector<int>> res;
        for (int i=0; i<k; i++) {
            res.push_back(pq.top());
            pq.pop();
        }

        return res;

    }
};
