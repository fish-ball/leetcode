class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int a[1001][1001] = {};
        int n = text1.size();
        int m = text2.size();
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                a[i][j] = max(a[i-1][j], a[i][j-1]);
                if (text1[i-1] == text2[j-1]) {
                    a[i][j] = max(a[i][j], a[i-1][j-1]+1);
                }
            }
        }
        return a[n][m];
    }
};
