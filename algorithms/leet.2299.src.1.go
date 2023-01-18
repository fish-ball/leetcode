// https://leetcode.cn/problems/strong-password-checker-ii/
// 2299. 强密码检验器 II
func strongPasswordCheckerII(password string) bool {
    // 判长度
    if len(password) < 8 { return false }
    // 判重
    for i:=1; i<len(password); i++ {
        if password[i] == password[i-1] { return false }
    }
    // 四种字符的存在
    d := [5]bool{}
    mp := map[rune]int{}
    for _, c := range "abcdefghijklmnopqrstuvwxyz" { mp[c] = 1 }
    for _, c := range "ABCDEFGHIJKLMNOPQRSTUVWXYZ" { mp[c] = 2 }
    for _, c := range "0123456789" { mp[c] = 3 }
    for _, c := range "!@#$%^&*()-+" { mp[c] = 4 }
    for _, c := range password { d[mp[c]] = true }
    return d[1] && d[2] && d[3] && d[4]
}
