// https://leetcode.cn/problems/generate-parentheses/
// 22. 括号生成

func generateParenthesis(n int) []string {
    b := []string{""}
    a1 := []int{0}
    a2 := []int{0}
    for k:=0; k<n+n; k++ {
        bb := []string{}
        aa1 := []int{}
        aa2 := []int{}
        for i, s := range b {
            l := a1[i]
            r := a2[i]
            if l > r && r < n {
                bb = append(bb, s + ")")
                aa1 = append(aa1, l)
                aa2 = append(aa2, r + 1)
            }
            if l < n {
                bb = append(bb, s + "(")
                aa1 = append(aa1, l+1)
                aa2 = append(aa2, r)
            }
        }
        b, a1, a2 = bb, aa1, aa2
    }
    return b
}
