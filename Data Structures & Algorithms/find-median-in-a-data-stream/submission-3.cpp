class MedianFinder {
public:
    MedianFinder() {}
    
    void addNum(int num) {
        max_pq.push(num);   
        // assure the biggest in max is smaller than the smallest in min
        if(!min_pq.empty() && max_pq.top() > min_pq.top()) {
            min_pq.push(max_pq.top());
            max_pq.pop();
        }

        if (max_pq.size() > min_pq.size() + 1) {
            min_pq.push(max_pq.top());
            max_pq.pop();
        }

        if (max_pq.size() + 1 < min_pq.size()) {
            max_pq.push(min_pq.top());
            min_pq.pop();
        }
    }
    
    double findMedian() {
        if (min_pq.size() == max_pq.size()) return (min_pq.top() + max_pq.top()) / 2.0;
        else if (min_pq.size() > max_pq.size()) return min_pq.top();
        else return max_pq.top();
    }

private:
    priority_queue<int> max_pq; // smaller number part
    priority_queue<int, vector<int>, greater<int>> min_pq;  // bigger number part
};
