class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int last[256];
        fill(begin(last), end(last), -1);

        int l = 0;
        int ans = 0;
        
        for (int r = 0; r < s.size(); r++) {
            unsigned char c = s[r];
            if (last[c] >= l) {
                l = last[c] + 1;
            }

            last[c] = r;
            ans = max(ans, r - l + 1);
        }

        return ans;

    }
};
