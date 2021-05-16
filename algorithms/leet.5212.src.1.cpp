class Solution {
public:
    int sumOfFlooredPairs(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; ++i) {
            int j = 0;
            // cout << "i = " << i << endl;
            while (j < n) {
                long long x = nums[j] / nums[i];
                vector<int>::iterator it = lower_bound(nums.begin() + j, nums.end(), nums[i] * (x + 1));
                int jj = it - nums.begin();
                // cout << "x = " << x << ", find = " << nums[i] * (x + 1) << ", j = " << j << ", jj = " << jj << endl;
                ans += x * (jj - j);
                ans %= 1000000007;
                j = jj;
            }
        }
        return (int)ans;
    }
};
