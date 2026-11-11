class Twitter {
public:
    Twitter() {
        time = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        tweet_map[userId].push_back({tweetId, time++});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> res; // output
        auto compare = [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0]; // maxHeap
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(compare)> pq(compare);
        follow_map[userId].insert(userId);
        for (auto followeeId : follow_map[userId]) {
            if (tweet_map.count(followeeId)) {  // check whether followee has posted
                int idx = tweet_map[followeeId].size() - 1;
                pq.push({tweet_map[followeeId][idx][1], tweet_map[followeeId][idx][0], followeeId, idx});
            }
        }

        while (!pq.empty() && res.size() < 10) {
            vector<int> cur = pq.top();
            pq.pop();
            res.push_back(cur[1]);
            int idx = cur[3];
            if (idx > 0) {
                pq.push({tweet_map[cur[2]][idx - 1][1], tweet_map[cur[2]][idx - 1][0], cur[2], idx - 1});
            }
        }

        return res;
    }
    
    void follow(int followerId, int followeeId) {
        // if (follow_map[followerId].empty()) follow_map[followerId].insert(followerId);
        follow_map[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        follow_map[followerId].erase(followeeId);
    }

private:
    int time;
    unordered_map<int, unordered_set<int>> follow_map;  // list of followees
    unordered_map<int, vector<vector<int>>> tweet_map; // tweet_id, time
};
