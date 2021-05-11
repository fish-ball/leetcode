class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int n = encoded.size() + 1;
        int x = 0;
        int y = 0;
        for (int i = 0; i < n-1; ++i) {
            x ^= encoded[i];
        }
        encoded.push_back(x);
        vector<int> ans(0);
        // k 是全集异或
        int k = 0;
        for (int i = 0; i < n; ++i) {
            k ^= i + 1;
        }
        x = y = 0;
        for (int i = 1; i < n; i += 2) {
            x ^= encoded[i];
            y ^= encoded[i+1];
        }
        for (int i = 0; i < n; ++i) {
            ans.push_back(x ^ k);
            x ^= encoded[(i+1)%n];
            x ^= encoded[(i+n)%n];
            swap(x, y);
        }
        return ans;
    }
};
