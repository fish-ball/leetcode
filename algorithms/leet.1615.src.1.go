// https://leetcode.cn/problems/maximal-network-rank/
// 1615. 最大网络秩

func maximalNetworkRank(n int, roads [][]int) int {
    ee := make([]int, n)
    g := [][]bool{}
    for i:=0; i<n; i++ {
        g = append(g, make([]bool, n))
    }
    for _, e := range roads {
        ee[e[0]]++
        ee[e[1]]++
        g[e[0]][e[1]] = true
        g[e[1]][e[0]] = true
    }
    ans := 0
    for i:=0; i<n; i++ {
        for j:=0; j<i; j++ {
            val := ee[i] + ee[j]
            if g[i][j] { val-- }
            if val > ans {
                ans = val
            }
        }
    }
    return ans
}
