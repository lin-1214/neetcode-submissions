class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> sub;


        dfs(0, s, sub, res);

        return res;
    }
private:
    void dfs(int idx, string& s, vector<string>& sub, vector<vector<string>>& res) {
        if (idx >= s.length()) {
            res.push_back(sub);
            return;
        }

        for (int j=idx; j<s.length(); j++) {
            if (isPali(idx, j, s)) {
                sub.push_back(s.substr(idx, j-idx+1));
                dfs(j+1, s, sub, res);
                sub.pop_back();
            }
        }
    }

    bool isPali(int l, int r, string& s) {
        while(l<r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }

        return true;
    }
};
