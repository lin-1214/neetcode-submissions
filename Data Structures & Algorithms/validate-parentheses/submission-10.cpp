class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> pr = {{')','('}, {']','['}, {'}','{'}};

        for (char c : s) {
            if (pr.count(c)) {
                if (stk.empty()) return false;
                if (stk.top() != pr[c]) return false;
                stk.pop();
            } else{
                stk.push(c);
            }
        }

        if (!stk.empty()) return false;

        return true;
    }
};
