class Solution {
public:
    bool isPalindrome(string s) {
        char l = 0;
        char r = s.size() - 1;

        while (l < r) {
            if (!isAlphabet(s[l])) {
                l++;
                continue;
            }

            if (!isAlphabet(s[r])) {
                r--;
                continue;
            }


            if (tolower(s[r--]) != tolower(s[l++])) return false;
        }

        return true;
    }

    bool isAlphabet(char c) {
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) return true;
        else return false;
    }
};

