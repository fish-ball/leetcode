// https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/
// 剑指 Offer 47. 礼物的最大价值

func maxValue(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])
    for i:=0; i<n; i++ {
        for j:=0; j<m; j++ {
            x := 0
            if i>0 && grid[i-1][j] > x {
                x = grid[i-1][j]
            }
            if j>0 && grid[i][j-1] > x {
                x = grid[i][j-1]
            }
            grid[i][j] += x
        }
    }
    return grid[n-1][m-1]
}
