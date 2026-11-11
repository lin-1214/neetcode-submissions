class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;

        while (l < r) {
            while (target - numbers[l] < numbers[r]) r--;

            while (target - numbers[r] > numbers[l]) l++;

            if ((numbers[l] + numbers[r]) == target) break;
        }

        return {l+1, r+1};
    }
};
