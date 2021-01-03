class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        multiset<int> s;
        vector<int> v(k, 0);
        vector<int> result(0);
        for (int i = 0; i < n; ++i) {
            if (s.size() >= k) {
                s.erase(s.find(v[i%k]));
            }
            v[i%k] = nums[i];
            s.insert(nums[i]);
            if (s.size() >= k) {
                result.push_back(*s.rbegin());
            }
        }
        return result;
    }
};
