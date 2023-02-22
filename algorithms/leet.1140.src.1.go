// https://leetcode.cn/problems/stone-game-ii/
// 1140. 石子游戏 II
// DP 或者记忆化搜索，做好状态压缩，计算剩下 x, m 位置的时候剩下可以得到的最大值

func stoneGameII(piles []int) int {
    n := len(piles)
    rem := make([]int, n+1)
    for i:=n-1; i>=0; i-- {
        rem[i] = rem[i+1] + piles[i]
    }
    // a, b 的 key 为 state, state = x * 1000 + m
    // 表示 a 或者 b 行动时，剩下 n-x 个石子可以选的情况下，各自可以得到的最高分数
    a := map[int]int{}
    var dfs func (int, int) int
    dfs = func (x, m int) int {
        if x == n { return 0 }
        ans := 0
        acc := 0
        state := x*1000+m
        if val, ok := a[state]; ok { return val }
        for xx:=1; xx<=m+m && x+xx<=n; xx++ {
            acc += piles[x+xx-1]
            mm := xx
            if mm < m { mm = m }
            if mm > n - x - xx { mm = n - x - xx }
            // fmt.Println(">>", x, m, xx, mm)
            val := acc + rem[x+xx] - dfs(x+xx, mm)
            if val > ans { ans = val }
        }
        a[state] = ans
        // fmt.Println(x, m, ans)
        return ans
    }
    return dfs(0, 1)
}
