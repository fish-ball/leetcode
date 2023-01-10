// https://leetcode.cn/problems/make-number-of-distinct-characters-equal/
// 2531. 使字符串总不同字符的数目相等
// 先做计数字典，然后遍历 26*26 暴力枚举

func isItPossible(word1 string, word2 string) bool {
    d1 := make(map[rune]int)
    d2 := make(map[rune]int)
    a1 := make([]rune, 0, len(d1))
    a2 := make([]rune, 0, len(d2))
    for _, x := range word1 { d1[x]++ }
    for _, x := range word2 { d2[x]++ }
    for x, _ := range d1 { a1 = append(a1, x) }
    for x, _ := range d2 { a2 = append(a2, x) }
    // 直接模拟
    for _, x := range a1 {
        for _, y := range a2 {
            c1 := len(d1)
            c2 := len(d2)
            if (x != y) {
                if d1[y] == 0 { c1 += 1 }
                if d1[x] == 1 { c1 -= 1 }
                if d2[x] == 0 { c2 += 1 }
                if d2[y] == 1 { c2 -= 1 }
            }
            if c1 == c2 { return true }
        }
    }
    return false
}
