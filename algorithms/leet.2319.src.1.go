// https://leetcode.cn/problems/check-if-matrix-is-x-matrix/
// 2319. 判断矩阵是否是一个 X 矩阵
func checkXMatrix(grid [][]int) bool {
    n := len(grid)
    for i:=0; i<n; i++ {
        if grid[i][i] == 0 || grid[i][n-1-i] == 0 {
            return false
        }
        for j:=i+1; j<n-1-i; j++ {
            if grid[i][j]!=0 || grid[j][i]!=0 || grid[n-1-i][j]!=0 || grid[j][n-1-i]!=0 {
                return false
            }
        }
    }
    return true
}
