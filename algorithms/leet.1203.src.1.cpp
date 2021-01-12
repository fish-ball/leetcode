class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        vector<int> ans(0);
        m = 0;
        map<int, int> mm;
        // 全部分块
        for (int i = 0; i < n; ++i) {
            if (group[i] == -1) {
                group[i] = m++;
            } else if(mm.find(group[i]) == mm.end()) {
                group[i] = mm[group[i]] = m++;
            } else {
                group[i] = mm[group[i]];
            }
        }
        // cout << "m = " << m << endl;
        
        // cout << "group = ";
        // for (int i = 0; i < n; ++i) {
        //     cout << group[i] << ' ';
        // }
        // cout << endl;

        // 构建原本入度图
        vector<set<int>> g1(n);
        vector<set<int>> h1(n);
        vector<int> in1(n);
        // 构建分块入度图
        vector<set<int>> g2(m);
        vector<set<int>> h2(m);
        vector<pair<int, int>> in2(0);
        vector<int> idx2(m);
        // 分块对点图
        vector<vector<int>> w(m);

        for (int i = 0; i < n; ++i) {
            w[group[i]].push_back(i);
            for (int j = 0; j < beforeItems[i].size(); ++j) {
                g1[beforeItems[i][j]].insert(i);
                h1[i].insert(beforeItems[i][j]);
                if (group[i] != group[beforeItems[i][j]]) {
                    g2[group[beforeItems[i][j]]].insert(group[i]);
                    h2[group[i]].insert(group[beforeItems[i][j]]);
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            in1[i] = h1[i].size();
        }


        // >>>>>
        // for (int i = 0; i < n; ++i) {
        //     cout << i << ": ";
        //     for (set<int>::iterator it = g1[i].begin(); it != g1[i].end(); ++it) {
        //         cout << *it << ' ';
        //     }
        //     cout << endl;
        // }
        // cout << ">>>" << endl;
        // for (int i = 0; i < m; ++i) {
        //     cout << i << ": ";
        //     for (set<int>::iterator it = g2[i].begin(); it != g2[i].end(); ++it) {
        //         cout << *it << ' ';
        //     }
        //     cout << endl;
        // }
        // <<<<<

        for (int i = 0; i < m; ++i) {
            in2.push_back(make_pair((int)h2[i].size(), i));
        }

        sort(in2.begin(), in2.end());
        for (int i = 0; i < m; ++i) {
            idx2[in2[i].second] = i;
        }
    

        for (int i = 0; i < m; ++i) {
            
            // >>>>>
            // for (int x = 0; x < m; ++x) {
            //     cout << in2[x].first << "/" << in2[x].second << "  ";
            // }
            // cout << endl;
            // <<<<<

            if (in2[i].first > 0) {
                // cout << "NOPE!" << endl;
                return vector<int>(0);
            }
            --in2[i].first;
            // 找到弹出的组为 k
            int k = in2[i].second;
            // cout << "pop* " << k << endl; 

            // 组内拓扑维护
            vector<pair<int, int>> p(0);
            map<int, int> idx1;
            for (int j = 0; j < w[k].size(); ++j) {
                p.push_back(make_pair(in1[w[k][j]], w[k][j]));
            }
            sort(p.begin(), p.end());
            for (int x = 0; x < p.size(); ++x) {
                idx1[p[x].second] = x;
            }

            // >>>>>
            // cout << "  * ";
            // for (int x = 0; x < p.size(); ++x) {
            //     cout << p[x].first << "/" << p[x].second << ' ';
            // }
            // cout << endl;
            // <<<<<

            for (int ii = 0; ii < p.size(); ++ii) {
                if (p[ii].first > 0) {
                    // cout << "NOPE2!!" << endl;
                    return vector<int>(0);
                }
                int iii = p[ii].second;
                // cout << "pop " << iii << endl;
                ans.push_back(iii);
                
                for (set<int>::iterator it = g1[iii].begin(); it != g1[iii].end(); ++it) {
                    int jjj = *it;
                    // cout << "deque " << jjj << endl;
                    --in1[jjj];
                    if (idx1.find(jjj) != idx1.end()) {
                        int _j = idx1[jjj];
                        --p[_j].first;
                        while(_j > 0 && p[_j].first < p[_j-1].first) {
                            swap(p[_j], p[_j-1]);
                            idx1[p[_j].second] = _j;
                            idx1[p[_j-1].second] = _j-1;
                            --_j;
                        }
                    }
                }
            }

            // cout << "idx2: ";
            // for (int x = 0; x < idx2.size(); ++x) {
            //     cout << idx2[x] << ' ';
            // }
            // cout << endl;

            // 分组拓扑维护
            for (set<int>::iterator it = g2[k].begin(); it != g2[k].end(); ++it) {
                int j = *it;
                // cout << "deque* " << j << endl;
                int _j = idx2[j];
                --in2[_j].first;
                
                while (_j > 0 && in2[_j].first < in2[_j-1].first) {
                    swap(in2[_j], in2[_j-1]);
                    idx2[in2[_j].second] = _j;
                    idx2[in2[_j-1].second] = _j-1;
                    --_j;
                }
            }
        }

        return ans;
    }
};
