class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        multiset<int> s;
        for (int i = 0; i < hand.size(); ++i) {
            s.insert(hand[i]);
        }
        while (s.size()) {
            int x = *s.begin();
            for (int i = 0; i < groupSize; ++i) {
                if(s.empty() || s.find(x + i) == s.end()) {
                    return false;
                }
                s.erase(s.find(x+i));
            }
        }
        return true;
    }
};
