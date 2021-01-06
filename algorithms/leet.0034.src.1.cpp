class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>::iterator l = lower_bound(nums.begin(), nums.end(), target);
        vector<int>::iterator r = upper_bound(nums.begin(), nums.end(), target);
        vector<int> result(0);
        result.push_back(l==r ? -1 : l-nums.begin());
        result.push_back(l==r ? -1 : r-nums.begin()-1);
        return result;
    }
};
