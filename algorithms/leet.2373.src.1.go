// https://leetcode.cn/problems/largest-local-values-in-a-matrix/
// 2373. 矩阵中的局部最大值

func largestLocal(grid [][]int) [][]int {
    n := len(grid)
    m := len(grid[0])
    for i:=0; i<n-2; i++ {
        for j:=0; j<m-2; j++ {
            for ii:=0; ii<3; ii++ {
                for jj:=0; jj<3; jj++ {
                    if grid[i+ii][j+jj] > grid[i][j] {
                        grid[i][j] = grid[i+ii][j+jj]
                    }
                }
            }
        }
        grid[i] = grid[i][:m-2]
    }
    return grid[:n-2]
}
