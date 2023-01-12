// https://leetcode.cn/problems/rearrange-characters-to-make-target-string/submissions/
// 2287. 重排字符形成目标字符串
// 简单题

func rearrangeCharacters(s string, target string) int {
    mp := map[rune]int{}
    mps := map[rune]int{}
    for _, c := range s { mps[c] += 1 }
    for _, c := range target { mp[c] += 1 }
    n := len(s) / len(target)
    for c, k := range mp {
        if mps[c] / k < n { n = mps[c] / k }
    }
    return n
}
