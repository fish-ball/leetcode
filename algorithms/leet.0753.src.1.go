// https://leetcode.cn/problems/cracking-the-safe/
// 构造图，具体一个密码数字为节点，存在向后滚动关系则为边
// 直接采用回溯法，就能很快搞定（猜想正确，不回证明）

func crackSafe(n int, k int) string {
    m := int16(1)
    for i:=0; i<n; i++ { m *= int16(k) }

    seq := []int16{0}
    visited := map[int16]bool{0: true}

    var dfs func(x int16) bool
    dfs = func(x int16) bool {
        // fmt.Println(x, seq)
        if len(seq) >= int(m) { return true }
        for i:=0; i<k; i++ {
            y := x * int16(k) % m + int16(i)
            if !visited[y] {
                visited[y] = true
                seq = append(seq, y)
                if dfs(y) { return true }
                seq = seq[:len(seq)-1]
                visited[y] = false
            }
        }
        return false
    }

    dfs(0)
    // fmt.Println(seq)
    sb := strings.Builder{}
    for i := 0;  i < n-1; i++ { sb.WriteRune('0') }
    for _, x := range seq { sb.WriteRune('0' + rune(x % int16(k))) }
    return sb.String()
}
