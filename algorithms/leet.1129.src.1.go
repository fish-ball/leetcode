// https://leetcode.cn/problems/shortest-path-with-alternating-colors/
// 1129. 颜色交替的最短路径 - 直接广搜即可，注意要区分两种颜色的状态
func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
    q := [][]int{}
    ans := make([]int, n, n)
    for i := range ans { ans[i] = -1 }
    q = append(q, []int{0, 0})
    b0 := make([]bool, n, n)
    b1 := make([]bool, n, n)
    b0[0] = true
    b1[0] = true
    mRed := make([][]int, n, n)
    mBlue := make([][]int, n, n)
    for i := range mRed { mRed[i] = make([]int, 0) }
    for i := range mBlue { mBlue[i] = make([]int, 0) }
    for i:=0; i<len(redEdges); i++ {
        e := redEdges[i]
        mRed[e[0]] = append(mRed[e[0]], e[1])
    }
    for i:=0; i<len(blueEdges); i++ {
        e := blueEdges[i]
        mBlue[e[0]] = append(mBlue[e[0]], e[1])
    }
    // fmt.Println(mRed, mBlue)
    for r:=n; len(q)>0 && r>0; {
        v, d := q[0][0], q[0][1]
        // fmt.Println(v,d)
        q = q[1:]
        if d >= 0 {
            if ans[v] == -1 {
                ans[v] = d
                r--
            }
            for _, w := range mRed[v] {
                // fmt.Println(" ", w)
                if !b1[w] {
                    b1[w] = true
                    q = append(q, []int{w, -d-1})
                }
            }
        }
        if d <= 0 {
            if ans[v] == -1 {
                ans[v] = -d
                r--
            }
            for _, w := range mBlue[v] {
                // fmt.Println(" ", w)
                if !b0[w] {
                    b0[w] = true
                    q = append(q, []int{w, -d+1})
                }
            }
        }
        
    }
    return ans
}
