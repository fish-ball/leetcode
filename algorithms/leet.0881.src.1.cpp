class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        multiset<int> s(people.begin(), people.end());
        int ans = 0;
        while (!s.empty()) {
            int x = limit - *s.rbegin();
            multiset<int>::iterator ii = s.end();
            s.erase(--ii);
            multiset<int>::iterator it = s.upper_bound(x);
            if (it != s.begin()) s.erase(--it);
            ans += 1;
        }
        return ans;
    }
};
