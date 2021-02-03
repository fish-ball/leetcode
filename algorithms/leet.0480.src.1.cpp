class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<pair<int, int> > s;
        multiset<pair<int, int> >::iterator it = s.begin();
        vector<double> ans;
        int a = 0;
        int b = 0;
        for (int i = 0; i < nums.size(); ++i) {

            // 如果要出栈，先出
            if (i >= k) {
                int y = nums[i-k];
                pair<int, int> yy = make_pair(y, k-i-1);
                multiset<pair<int, int> >::iterator it3 = s.find(yy);
                if (it3 == it) {
                    ++it;
                    b -= 1;
                } else if (it == s.end() || yy < *it) {
                    a -= 1;
                } else {
                    b -= 1;
                }
                s.erase(it3);
            }
            
            // 插入一个
            int x = nums[i];
            pair<int, int> xx = make_pair(x, -i-1);
            multiset<pair<int, int> >::iterator it2 = s.insert(xx);
            if (it == s.end()) {
                a += 1;
            } else if (xx < *it) {
                a += 1;
            } else {
                b += 1;
            }

            // 调整位置
            if (a + b == k) {
                while(a > (k-1) / 2) {
                    --it;
                    a -= 1;
                    b += 1;
                }
                while(a < (k-1) / 2) {
                    ++it;
                    a += 1;
                    b -= 1;
                }
                multiset<pair<int, int> >::iterator it2 = it;
                ++it2;
                ans.push_back(k%2 ? (double)it->first : 0.5*it2->first + 0.5*it->first);
            }
        }
        return ans;
    }
};
