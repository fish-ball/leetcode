// https://leetcode.cn/problems/separate-black-and-white-balls/

class Solution {
public:
    long long minimumSteps(string s) {
        long long ans = 0;
        int x = 0;  // Ones count ever seen.
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '1') {
                x += 1;
            } else {
                ans += x;
            }
        }
        return ans;
    }
};
