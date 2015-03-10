public class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ans = new int[n][n];
        for(int[] row: ans) Arrays.fill(row, -1);
        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };
        int d = 0, x = 0, y = 0;
        for(int i = 0; i < n * n; ++i) {
            ans[x][y] = i + 1;
            if( 0 <= x + dx[d] && x + dx[d] < n && 
                0 <= y + dy[d] && y + dy[d] < n && 
                ans[x + dx[d]][y + dy[d]] == -1) {
            } else {
                d = d + 1 & 3;
            }
            x += dx[d];
            y += dy[d];
        }
        return ans;
    }
}
