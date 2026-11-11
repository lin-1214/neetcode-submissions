class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        for (int stone : stones) {
            pq.push(stone);
        }

        int remain;

        while(pq.size() >= 2) {
            int heaviest = pq.top();
            pq.pop();
            int sec_heaviest = pq.top();
            pq.pop();

            remain = heaviest - sec_heaviest;
            pq.push(remain);
        }

        return remain;
    }
private:
    priority_queue<int> pq;
};
