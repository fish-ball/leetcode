// https://leetcode.cn/problems/count-asterisks/
// 2315. 统计星号

func countAsterisks(s string) int {
    flag := true
    ans := 0
    for _, c := range s {
        switch c {
        case '|': flag = !flag
        case '*': if flag { ans++ }
        }
    }
    return ans
}
