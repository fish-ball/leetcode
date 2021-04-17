class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (!k) return false;
        multiset<long long> s;
        s.insert(0x7FFFFFFFFFFFFFFLL);
        s.insert(-0x7FFFFFFFFFFFFFFLL);
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k) {
                // cout << "pop: " << nums[i-k-1] << endl;
                s.erase(s.find(nums[i-k-1]));   
            }
            // cout << "push: " << nums[i] << endl;
            multiset<long long>::iterator it = s.insert(nums[i]);
            // cout << *prev(it) << ' ' << *it << ' ' << *next(it) << endl;
            if (*it - *prev(it) <= t || *next(it) - *it <= t) {
                return true;
            }
        }
        return false;
    }
};
