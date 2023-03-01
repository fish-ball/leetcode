// https://leetcode.cn/problems/maximum-score-words-formed-by-letters/
// 1255. 得分最高的单词集合

func maxScoreWords(words []string, letters []byte, score []int) int {
    n := len(words)
    ans := 0
    // 基础分
    scores := make([]int, n)
    for i:=0; i<n; i++ {
        for _, c := range words[i] {
            scores[i] += score[int(c-'a')]
        }
    }
    // 剩余的字母计数
    rem := make([]int, 26)
    for _, b := range letters {
        rem[int(rune(b)-'a')]++
    }
    // 用格雷码遍历，就可以每次只 diff 一个
    acc := 0
    mask := 0
    for i:=1; i<(1<<n); i++ {
        // 格雷法的翻转掩码
        diff := i&^(i-1)
        mask ^= diff
        // 翻转掩码的翻转位
        j := 0
        for diff&(1<<j) == 0 { j++ }
        // 确定翻转位是打开还是关闭
        if mask & diff > 0 { // 打开
            for _, c := range words[j] { rem[int(c-'a')]-- }
            acc += scores[j]
        } else { // 关闭
            for _, c := range words[j] { rem[int(c-'a')]++ }
            acc -= scores[j]
        }
        // 如果结果不比最优解好，直接跳过
        if acc < ans { continue }
        // 校验是否可行解（不存在负数）
        valid := true
        for _, x := range rem { valid = valid && x>=0 }
        if valid { ans = acc }
    }
    return ans
}
