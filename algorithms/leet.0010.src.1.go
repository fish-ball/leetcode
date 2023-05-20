// https://leetcode.cn/problems/regular-expression-matching/submissions/
// 因为字符串最长才 20，直接暴力递归可以过

func isMatch(s string, p string) bool {
    if s == "" {
        if len(p) > 1 && p[1] == '*' {
            return isMatch("", p[2:])
        }
        return p == ""
    }
    if p == "" { return false }
    if len(p)>1 && p[1] == '*' {
        if isMatch(s, p[2:]) { return true }
        for i:=0; i<len(s) && (p[0]=='.' || s[i]==p[0]); i++ {
            if isMatch(s[i+1:], p[2:]) { return true }
        }
        return false
    }
    if p[0] == '.' || s[0] == p[0] { return isMatch(s[1:], p[1:]) }
    return false
}
