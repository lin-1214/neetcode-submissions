class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        for (auto &str: strs) {
            vector<int> count(26, 0);
            for (auto &c: str) {
                count[c - 'a']++;
            }

            string key = to_string(count[0]);
            for (int i = 1; i < 26; i++) {
                key += ',' + to_string(count[i]);
            }
            map[key].push_back(str);
        }

        vector<vector<string>> res;
        for (auto &g : map) {
            res.push_back(g.second);
        }

        return res;
    }
};
