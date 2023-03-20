// https://leetcode.cn/problems/numbers-with-repeated-digits/
// 1012. 至少有 1 位重复的数字

func numDupDigitsAtMostN(n int) int {
    ans := n
    acc := 0
    // 以    3456789 为例：
    // dec = 1000000, m = 6
    dec, m := 1, 0
    for ; dec*10 <= n; m++ { dec *= 10 }
    // fmt.Println("n =", n, ", dec =", dec, ", m =", m)
    // 第一段，from 1 to 999999
    // fmt.Println("Stage 1:")
    for i:=1; i<=m; i++ {
        // 一共 i 位开头任意填
        // 例如 i=6 时，应该有 9*9*8*7*6*5 种
        acc = 9
        for j:=0; j<i-1; j++ { acc *= 9-j }
        // fmt.Println("+", acc)
        ans -= acc
    }
    // fmt.Println("ans =", ans)
    // fmt.Println("Stage 2:")
    // 第二段，from 1000000 ~ 2999999
    acc = 1
    for i:=0; i<m; i++ {
        // 例如：从 1000000 到 1999999
        // 共有 9*8*7*6*5*4
        acc *= 9-i
    }
    // fmt.Println("+", acc, "*", n / dec - 1)
    ans -= (n / dec - 1) * acc
    // 第三段，from 3000000 ~ 3399999
    // fmt.Println("Stage 3:")
    visited := map[int]bool{}
    for dec > 0 {
        head := n / dec
        // fmt.Println("dec =", dec, ", head =", head)
        if visited[head] { break }
        visited[head] = true
        n %= dec
        dec /= 10
        m--

        acc = 1
        // fmt.Println("n =", n, ", m =", m, ",", visited)
        for i:=0; i<m; i++ {
            acc *= 9-len(visited)-i
        }
        k := 0
        if dec == 0 { 
            k = 1
        } else {
            for i:=0; i < n / dec; i++ {
                if !visited[i] { k++ }
            }
        }
        // fmt.Println("+", acc, "*", k)
        ans -= k * acc
    }
    return ans
}
