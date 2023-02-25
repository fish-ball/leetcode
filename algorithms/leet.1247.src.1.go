// https://leetcode.cn/problems/minimum-swaps-to-make-strings-equal/
// 1247. 交换字符使得字符串相同

func minimumSwap(s1 string, s2 string) int {
    a, b := 0, 0
    for i, x := range s1 {
        y := rune(s2[i])
        if x == y { continue }
        if x == 'x' { a++ } else { b++ }
    }
    if (a^b)&1 == 1 { return -1 }
    if a&1 == 1 { return a/2+b/2+2 }
    return a/2 + b/2
}
