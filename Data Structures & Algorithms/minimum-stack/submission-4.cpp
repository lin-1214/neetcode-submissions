class MinStack {
private:
    stack<int> stk;
    stack<int> mins;
public:
    MinStack() {}
    
    void push(int val) {
        stk.push(val);
        if (mins.empty()) mins.push(val);
        else mins.push(min(val, mins.top()));
    }
    
    void pop() {
        stk.pop();
        mins.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return mins.top();
    }
};
