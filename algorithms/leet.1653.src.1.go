// https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
// 1653. 使字符串平衡的最少删除次数

func minimumDeletions(s string) int {
    n := len(s)
    a := 0
    acc := make([]int, n)
    for i, x := range s {
        if x == 'a' {
            a++
            acc[i] = a
        }
    }
    ans := a
    for i, x := range acc {
        if (i+1-x) + (a-x) < ans {
            ans = (i+1-x) + (a-x)
        }
    }
    return ans
}
