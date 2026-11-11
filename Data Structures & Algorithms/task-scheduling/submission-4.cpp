class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26, 0);
        for (auto task : tasks) {
            count[task - 'A']++;
        }

        priority_queue<int> pq;
        for (auto cnt : count) {
            if (cnt > 0) pq.push(cnt);
        }

        int time = 0;

        // remain task, available time
        queue<pair<int, int>> q;

        while(!pq.empty() || !q.empty()) {
            time++;

            if (!pq.empty()) {
                int cnt = pq.top() - 1;
                pq.pop();
                if (cnt > 0) q.push({cnt, time + n}); // Only handle the cnt > 0 case
            } else {
                time = q.front().second;
            }

            if (!q.empty() && q.front().second == time) {
                pq.push(q.front().first);
                q.pop();
            }
        }

        return time;
    }
};
