// https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/
// 1210. 穿过迷宫的最少移动次数

type State struct {
    d, x, y, k int
}

func minimumMoves(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])
    dp := [][][]int{}
    for i:=0; i<2; i++ {
        dp = append(dp, [][]int{})
        for j:=0; j<n; j++ {
            dp[i] = append(dp[i], make([]int, m, m))
        }
    }
    for i:=0; i<2; i++ {
        for j:=0; j<n; j++ {
            for k:=0; k<n; k++ {
                dp[i][j][k] = -1
            }
        }
    }
    // 入队
    dp[0][0][0] = 0
    q := []*State{&State{0, 0, 0, 0}}

    enqueue := func(d, x, y, k int) {
        if dp[d][x][y] > -1 { return }
        dp[d][x][y] = k
        q = append(q, &State{d, x, y, k})
    }
    
    for len(q) > 0 {
        // pop
        s := q[0]
        q = q[1:]
        if s.x == n-1 && s.y == m-2 && s.d == 0 { return s.k }
        if s.d == 0 {
            if s.y+2<m && grid[s.x][s.y+2]==0 { 
                enqueue(0, s.x, s.y+1, s.k+1)
            }
            if s.x+1<n && s.y+1<m && grid[s.x+1][s.y]+grid[s.x+1][s.y+1]==0 {
                enqueue(1, s.x, s.y, s.k+1)
                enqueue(0, s.x+1, s.y, s.k+1)
            }
        } else if s.d == 1 {
            if s.x+2<n && grid[s.x+2][s.y]==0 { 
                enqueue(1, s.x+1, s.y, s.k+1)
            }
            if s.x+1<n && s.y+1<m && grid[s.x][s.y+1]+grid[s.x+1][s.y+1]==0 {
                enqueue(0, s.x, s.y, s.k+1)
                enqueue(1, s.x, s.y+1, s.k+1)
            }
        }
    }
    
    return -1
}
