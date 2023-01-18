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
    ans := 0
    for _, c := range password {
        switch {
            case 'a' <= c && c <= 'z': ans |= 1
            case 'A' <= c && c <= 'Z': ans |= 2
            case '0' <= c && c <= '9': ans |= 4
            case strings.ContainsRune("!@#$%^&*()-+", c): ans |= 8
        }
    }
    return ans == 15
}
