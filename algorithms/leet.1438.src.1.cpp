class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        if (!nums.size()) return 0;
        multiset<int> S;
        int ans = 0;
        int j = 0;
        for (int i = 0; i < nums.size(); ++i) {
            S.insert(nums[i]);
            while (j <= i && *S.rbegin() - *S.begin() > limit) {
                S.erase(S.find(nums[j]));
                j += 1;
            }
            ans = max(ans, i-j+1);
        }
        return ans;
    }
};
